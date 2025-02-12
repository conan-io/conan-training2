from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMakeToolchain, CMakeDeps
from conan.tools.build import valid_min_cppstd
from conan.errors import ConanInvalidConfiguration


class FormatterRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    options = {"with_tabulate": [True, False]}
    default_options = {"with_tabulate": False}

    def validate(self):
        if (self.options.with_tabulate and
                valid_min_cppstd(self, 17)):
            raise ConanInvalidConfiguration("Tabulate requires C++17")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.cache_variables["USE_TABULATE"] = self.options.with_tabulate
        tc.generate()

        cd = CMakeDeps(self)
        cd.generate()

    def requirements(self):
        if self.options.with_tabulate:
            self.requires("tabulate/1.5")
        else:
            self.requires("fmt/11.0.2")


    def layout(self):
        cmake_layout(self)
