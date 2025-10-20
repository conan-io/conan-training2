import json
from conan.api.conan_api import ConanAPI
from conan.api.model import ListPattern
from conan.api.output import cli_out_write, ConanOutput

from conan.api.output import ConanOutput, Color
from conan.cli.command import conan_command, OnceArgument
import argparse

# Colors for output
package_color = Color.BRIGHT_BLUE
version_color = Color.BRIGHT_GREEN
info_color = Color.BRIGHT_CYAN

def json_export(data):
    cli_out_write(json.dumps({"cache_path": data}))

@conan_command(group="Custom commands", formatters={"json": json_export, "text": cli_out_write})
def info_custom(conan_api: ConanAPI, parser, *args):
    """
    Shows detailed information about installed packages with customizable output formats.
    """
    parser.add_argument("package", help="Package name to get info for")
    parser.add_argument("--format", choices=["text", "json"], 
                       default="text", help="Output format")
    parser.add_argument("--show-deps", action="store_true", 
                       help="Show dependencies and package details")
    parser.add_argument("--remote", action=OnceArgument,
                       help="Search in the specified remote instead of local cache")
    
    args = parser.parse_args(*args)
    
    out = ConanOutput()
    remote = conan_api.remotes.get(args.remote) if args.remote else None
    output_source = remote or "Local cache"
    
    try:
        # Use Conan's list API with pattern matching
        pattern = f"*{args.package}*/*#*:*#*"
        pkg_list = conan_api.list.select(ListPattern(pattern, rrev=None, prev=None), remote=remote)
        
        if not pkg_list:
            return {"error": f"No packages found matching '{args.package}' in {output_source}"}
        
        package_info = []
        
        # Process each recipe revision
        for sub_pkg_list in pkg_list.split():
            for rref, packages in sub_pkg_list.items():
                # Get unique package IDs for this recipe
                unique_package_ids = {p.package_id for p in packages}
                
                for pkg_id in unique_package_ids:
                    # Get the latest package revision for this package_id
                    latest_pkg = max([p for p in packages if p.package_id == pkg_id], 
                                   key=lambda p: p.timestamp)
                    
                    package_data = {
                        "name": rref.name,
                        "version": rref.version,
                        "user": rref.user,
                        "channel": rref.channel,
                        "recipe_revision": str(rref.revision),
                        "package_id": latest_pkg.package_id,
                        "package_revision": str(latest_pkg.revision),
                        "timestamp": latest_pkg.timestamp.isoformat() if latest_pkg.timestamp else None,
                        "source": output_source
                    }
                    package_info.append(package_data)
        
        # Return data for formatters to handle
        return {
            "packages": package_info,
            "show_deps": args.show_deps,
            "format": args.format
        }
            
    except Exception as e:
        return {"error": str(e)}
