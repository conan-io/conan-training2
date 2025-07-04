import os
from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout
from conan.tools.files import copy


class SecureScannerRecipe(ConanFile):
    name = "secure-scanner"
    version = "1.0"
    package_type = "application"

    settings = "os", "compiler", "build_type", "arch"

    exports_sources = "CMakeLists.txt", "src/*"

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        ext = ".exe" if self.settings_build.os == "Windows" else ""
        copy(self, f"secure-scanner{ext}", self.build_folder,
             os.path.join(self.package_folder, "bin"), keep_path=False)

    def package_info(self):
        self.buildenv_info.define("MY_VAR", "42")

    def package_id(self):
        del self.info.settings.compiler
        del self.info.settings.build_type
