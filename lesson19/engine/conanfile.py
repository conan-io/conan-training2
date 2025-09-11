from conan import ConanFile


class Engine(ConanFile):
    name = "engine"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"

    package_type = "shared-library"

    def requirements(self):
        self.requires("math/1.0")
