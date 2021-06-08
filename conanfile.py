import os
from conans import ConanFile, CMake

class IgeConan(ConanFile):
    name = 'json'
    version = '3.9.1'
    license = "MIT"
    author = "Indi Games"
    url = "https://github.com/indigames"
    description = name + " library for IGE Engine"
    topics = ("#Python", "#IGE", "#Games")
    settings = []
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake_find_package"
    exports_sources = "*.h*"
    no_copy_source = True
    requires = []
    short_paths = True

    def package(self):
        self.copy("*.h*", dst="include", src="single_include")

    def package_id(self):
        self.info.header_only()
