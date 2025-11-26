
def pre_export(conanfile):
    if not conanfile.license:
        conanfile.output.error("Recipe does not define its 'license'")
