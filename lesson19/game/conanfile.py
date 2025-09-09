from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class gameRecipe(ConanFile):
    name = "game"
    version = "1.0"
    package_type = "application"

    settings = "os", "compiler", "build_type", "arch"

    requires = "engine/1.0"
