from conan.tools.files import copy
import os


def deploy(graph, output_folder, **kwargs):
    for name, dep in graph.root.conanfile.dependencies.items():
        copy(
            graph.root.conanfile,
            "*",
            os.path.join(str(dep.folders.package_folder), "licenses"),
            os.path.join(output_folder, "licenses", str(dep.ref.name), str(dep.ref.version))
        )
