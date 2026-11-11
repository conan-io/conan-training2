from conan import ConanFile


class Network(ConanFile):
    name = "network"
    version = "1.0"
    package_type = "static-library"
    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        self.requires("fmt/12.0.0")
