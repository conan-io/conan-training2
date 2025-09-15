from conan import ConanFile


class Math(ConanFile):
    name = "math"
    version = "1.0"
    package_type = "library"
    settings = "os", "compiler", "build_type", "arch"

    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "header_only": [True, False]
    }
    default_options = {
        "shared": False,
        "fPIC": True,
        "header_only": False
    }

    # def config_options(self):
    #     if self.settings.os == "Windows":
    #         self.options.rm_safe("fPIC")

    # def configure(self):
    #     if self.options.get_safe("shared") or self.options.header_only:
    #         self.options.rm_safe("fPIC")
    #     if self.options.header_only:
    #         self.options.rm_safe("shared")

    # def package_id(self):
    #     if self.info.options.header_only:
    #         self.info.clear()
