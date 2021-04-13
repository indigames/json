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
    exports_sources = "*"
    no_copy_source = True
    short_paths = True

    def package(self):
        dirs = os.listdir(os.environ['PROJECT_DIR'])
        print(dirs)
        if 'include' in dirs:
            exports_sources = "include/*"
            print(exports_sources)
        self.copy("*.h*")

    def package_id(self):
        self.info.header_only()