import json

from conan.api.conan_api import ConanAPI
from conan.api.output import cli_out_write
from conan.cli.command import conan_command


def output_json(results):
    cli_out_write(json.dumps(results, indent=4))


def output_default(results):
    for profile, contents in results.items():
        cli_out_write(f"Occurrence found in profile '{profile}':")
        cli_out_write(contents)


@conan_command(
    group="Misc. Utils", formatters={"json": output_json, "text": output_default}
)
def search_profiles(conan_api: ConanAPI, parser, *args):
    """
    Command to search for a string ocurrence inside all Conan profiles.
    """
    parser.add_argument("query", help="Search query.")
    args = parser.parse_args(*args)
    query = args.query.lower()
    results = {}
    profiles = conan_api.profiles.list()
    for profile in profiles:
        computed_profile = str(conan_api.profiles.get_profile([profile]))
        if query in computed_profile.lower():
            results[profile] = computed_profile
    return results
