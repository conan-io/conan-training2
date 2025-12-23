import json
import os
from conan.tools.sbom import cyclonedx_1_6

def post_package(conanfile, **kwargs):
    sbom_cyclonedx_1_6 = cyclonedx_1_6(conanfile)
    metadata_folder = conanfile.package_metadata_folder
    file_name = "sbom.cdx.json"
    with open(os.path.join(metadata_folder, file_name), 'w') as f:
        json.dump(sbom_cyclonedx_1_6, f, indent=4)
    conanfile.output.success(f"CYCLONEDX CREATED - {conanfile.package_metadata_folder}")
