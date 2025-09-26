import os
from conan import ConanFile
from conan.tools.files import copy


class Conf(ConanFile):
    name = "myconf"
    version = "0.1"
    settings = "os"
    package_type = "configuration"

    def package(self):
        folder = "win" if self.settings.os == "Windows" else "unix"
        copy(
            self,
            "*",
            src=os.path.join(self.build_folder, "profiles", folder),
            dst=os.path.join(self.package_folder, "profiles"),
        )
