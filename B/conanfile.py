from conans import ConanFile


class BB(ConanFile):
    name = "BB"
    settings = "os", "compiler", "build_type", "arch"
    description = "None"
    url = "None"
    license = "None"
    author = "None"
    generators = "virtualenv", "json", "cmake_find_package"
    version = "1.0.0"