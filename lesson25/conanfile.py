from conan import ConanFile
from conan.tools.cmake import cmake_layout

class FormatterRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"
    # license = None  # Removed license for demostration purposes

    def requirements(self):
        self.requires("fmt/11.2.0")

    def build_requirements(self):
        self.tool_requires("cmake/3.31.5")

    def layout(self):
        cmake_layout(self)
