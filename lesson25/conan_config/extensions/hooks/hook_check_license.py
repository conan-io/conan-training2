
def pre_export(conanfile, **kwargs):
    if not conanfile.license:
        conanfile.output.error("Recipe does not define its 'license'")
