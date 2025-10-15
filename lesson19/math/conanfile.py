from conan import ConanFile


class Math(ConanFile):
    name = "math"
    version = "1.0"
    package_type = "static-library"
    settings = "os", "compiler", "build_type", "arch"
