from conan import ConanFile


class PyReq(ConanFile):
    name = "pyreq"
    version = "1.0"
    package_type = "python-require"


# Module-level variables and functions
myvar = 123

def myfunct():
    return 234


# Base class for other recipes to inherit
class MyCompanyBase:
    license = "Proprietary - MyCompany Inc."
    author = "MyCompany"
    settings = "os", "compiler", "build_type", "arch"

    def build(self):
        self.output.info("MyCompanyBase build!")
