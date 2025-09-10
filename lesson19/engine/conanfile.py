from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class Engine(ConanFile):
    name = "engine"
    version = "1.0"
    settings = "build_type"
    package_type = "shared-library"

    def requirements(self):
        self.requires("math/1.0")
