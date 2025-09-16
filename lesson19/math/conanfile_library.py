from conan import ConanFile


class Math(ConanFile):
    name = "math"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"

    package_type = "library"

    options = {"shared": [True, False], "header_only": [True, False]}
    default_options = {"shared": False, "header_only": False}
