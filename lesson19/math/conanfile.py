from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class mathRecipe(ConanFile):
    name = "math"
    version = "1.0"
    package_type = "static-library"
