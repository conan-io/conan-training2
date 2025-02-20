from conan import ConanFile
from conan.tools.cmake import cmake_layout

class FormatterRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires("fmt/11.0.2")
    
    def layout(self):
        cmake_layout(self)
