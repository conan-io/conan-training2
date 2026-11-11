from conan import ConanFile


class App(ConanFile):
    name = "app"
    version = "1.0"
    package_type = "application"
    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        self.requires("parser/1.0")
        self.requires("network/1.0")
        # Uncomment to resolve the version conflict
        # self.requires("fmt/12.0.0", override=True)
