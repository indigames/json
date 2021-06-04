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
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"
    exports_sources = "*.h*"
    no_copy_source = True
    short_paths = True

    def package(self):
        self.copy("*.h*", dst="include", src="single_include")
        self.run(f'conan upload {self.name}/{self.version}@ige/test --remote ige-center --force --confirm')

    def package_id(self):
        self.info.header_only()
