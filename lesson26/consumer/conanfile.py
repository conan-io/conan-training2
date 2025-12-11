from conan import ConanFile


class ConsumerRecipe(ConanFile):
    name = "consumer"
    version = "1.0"

    python_requires = "pyreq/[>=1.0 <2.0]"
    python_requires_extend = "pyreq.MyCompanyBase"

    # license, author, settings and build() inherited from MyCompanyBase

    def generate(self):
        # Access module-level variables and functions
        pyreq = self.python_requires["pyreq"].module
        self.output.info(f"myvar: {pyreq.myvar}")
        self.output.info(f"myfunct(): {pyreq.myfunct()}")

        # Access inherited attributes from MyCompanyBase
        self.output.info(f"license: {self.license}")
        self.output.info(f"author: {self.author}")
