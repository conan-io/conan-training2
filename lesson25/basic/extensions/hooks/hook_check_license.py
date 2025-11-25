
def pre_export(conanfile):
    if not hasattr(conanfile, "license"):
        conanfile.output.error("Recipe does not have a 'license'")
