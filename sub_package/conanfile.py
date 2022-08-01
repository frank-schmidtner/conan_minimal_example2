from conans import ConanFile


class SubPackage(ConanFile):
    name = "sub_package"
    settings = "os", "compiler", "build_type", "arch"
    description = "None"
    url = "None"
    license = "None"
    author = "None"
    generators = "virtualenv", "json", "cmake_find_package"
    version = "1.0.0"

    def requirements(self):
        self.requires("sub_package2/1.0.0@test/test")