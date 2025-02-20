from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMakeToolchain, CMakeDeps
from conan.tools.build import valid_min_cppstd
from conan.errors import ConanInvalidConfiguration


class FormatterRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    options = {"with_std_format": [True, False]}
    default_options = {"with_std_format": False}

    def validate(self):
        if (self.options.with_std_format and
                not valid_min_cppstd(self, 20)):
            raise ConanInvalidConfiguration("std::format requires C++20")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.cache_variables["USE_STD_FORMAT"] = self.options.with_std_format
        tc.generate()

        cd = CMakeDeps(self)
        cd.generate()

    def requirements(self):
        if not self.options.with_std_format:
            self.requires("fmt/11.0.2")

    def layout(self):
        cmake_layout(self)
