from conans import ConanFile

class SubSubPackage(ConanFile):
    name = "sub_sub_package"
    description = "None"
    settings = "os", "compiler", "build_type", "arch"
    description = "None"
    url = "None"
    license = "None"
    author = "None"
    generators = "virtualenv", "json", "cmake_find_package"
    version = "1.0.0"
