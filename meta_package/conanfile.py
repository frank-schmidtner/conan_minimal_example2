from conans import ConanFile


class MetaPackage(ConanFile):
    name = "meta_package"
    settings = "os", "compiler", "build_type", "arch"
    description = (
        "Meta package"
    )
    url = "None"
    license = "None"
    author = "None"
    generators = "virtualenv", "json", "cmake_find_package"
    version = "1.0.0"

    def build_requirements(self):
        self.build_requires("sub_package2/1.0.0@test/test")

    def requirements(self):
        self.requires("sub_package/1.0.0@test/test")