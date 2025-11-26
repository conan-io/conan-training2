
def pre_export(conanfile):
    if not getattr(conanfile, "license", None):
        conanfile.output.error("Recipe does not define its 'license'")
