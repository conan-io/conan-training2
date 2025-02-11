from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMakeToolchain, CMakeDeps

class FormatterRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    options = {"with_tabulate": [True, False]}
    default_options = {"with_tabulate": False}

    def requirements(self):
        if self.options.with_tabulate:
            self.requires("tabulate/1.5")
        else:
            self.requires("fmt/11.0.2")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.cache_variables["USE_TABULATE"] = self.options.with_tabulate
        tc.generate()

        cd = CMakeDeps(self)
        cd.generate()

    def layout(self):
        cmake_layout(self)
