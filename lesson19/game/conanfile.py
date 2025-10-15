from conan import ConanFile


class Game(ConanFile):
    name = "game"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"

    package_type = "application"


    def requirements(self):
        self.requires("engine/1.0")
