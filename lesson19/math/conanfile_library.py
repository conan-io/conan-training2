from conan import ConanFile


class Math(ConanFile):
    name = "math"
    version = "1.0"
    package_type = "library"
    settings = "os", "compiler", "build_type", "arch"

    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "header_only": [True, False]
    }
    default_options = {
        "shared": False,
        "fPIC": True,
        "header_only": True
    }
