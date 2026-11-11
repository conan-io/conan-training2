from conan import ConanFile


class Parser(ConanFile):
    name = "parser"
    version = "1.0"
    package_type = "static-library"
    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        self.requires("fmt/[>=11.0 <13]")
