from conans import ConanFile


class AA(ConanFile):
    name = "AA"
    settings = "os", "compiler", "build_type", "arch"
    description = "None"
    url = "None"
    license = "None"
    author = "None"
    generators = "virtualenv", "json", "cmake_find_package"
    version = "1.0.0"

    def requirements(self):
        self.requires("BB/1.0.0@test/test")
        self.requires("CC/1.0.0@test/test")