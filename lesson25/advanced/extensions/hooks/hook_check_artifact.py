from pathlib import Path
from conan.errors import ConanException

def post_package(conanfile):
    package_folder = Path(conanfile.package_folder)
    invalid_files = [p.relative_to(package_folder) for p in package_folder.glob("**/*.cmake")]
    if invalid_files:
        raise ConanException(
            "CMake config files found in package, Conan recomends "
            "using 'package_info()' to define proper usage requirements"
        )
