from conans import ConanFile


class CC(ConanFile):
    name = "CC"
    settings = "os", "compiler", "build_type", "arch"
    description = "None"
    url = "None"
    license = "None"
    author = "None"
    generators = "virtualenv", "json", "cmake_find_package"
    version = "1.0.0"

    def build_requirements(self):
        self.tool_requires("BB/1.0.0@test/test")