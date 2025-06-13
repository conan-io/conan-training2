import os
from conan import ConanFile
from conan.tools.files import copy


class helloRecipe(ConanFile):
    name = "hello"
    version = "0.1"
    settings = "os", "arch"

    def layout(self):
        _os = str(self.settings.os).lower()
        _arch = str(self.settings.arch).lower()
        self.folders.build = os.path.join("vendor_hello_library", _os, _arch)
        self.folders.source = self.folders.build

    def package(self):
        copy(self, "*.h", os.path.join(self.build_folder, "include"),
             os.path.join(self.package_folder, "include"), keep_path=False)
        copy(self, "*.lib", self.build_folder, os.path.join(self.package_folder, "lib"), keep_path=False)
        copy(self, "*.a", self.build_folder, os.path.join(self.package_folder, "lib"), keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]
