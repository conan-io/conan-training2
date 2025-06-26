from conan import ConanFile
from conan.tools.layout import basic_layout
from conan.tools.files import copy

class helloRecipe(ConanFile):
    name = "hello"
    version = "1.0"
    package_type = "header-library"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of hello package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "include/*"

    def package_id(self):
        self.info.clear()

    def layout(self):
        basic_layout(self)

    def package(self):
        copy(self, "include/*", self.source_folder, self.package_folder)

    def package_info(self):
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
