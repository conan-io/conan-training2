from conan import ConanFile


class SecureScannerTestRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    def build_requirements(self):
        self.tool_requires(self.tested_reference_str)

    def build(self):
        var_cmd = (
            "set MY_VAR"
            if self.settings_build.os == "Windows"
            else "echo MY_VAR=$MY_VAR"
        )
        self.run(var_cmd)

    def test(self):
        self.run("secure-scanner mypath")