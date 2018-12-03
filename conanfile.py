#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os
import shutil


class QtBinaryConan(ConanFile):
    name = "Qt"
    version = "5.11.2"
    description = "Qt binary distributed by Qt company"
    topics = "conan", "qt"
    url = "https://gitlab.clarisys.fr/common/conan-qtbinary"
    homepage = "https://www.qt.io/"
    author = "Laurent Coustet <ed@zehome.com>"
    license = "GPL-3.0-only"
    generators = "txt"
    settings = "os", "compiler", "build_type", "arch"

    def package(self):
        QTSRC = self.env["QT_DIR"]
        for d in ("bin", "include", "lib", "libexec",
            "mkspecs", "phrasebooks", "plugins", "qml",
            "qtvirtualkeyboard", "resources", "translations"
        ):
            self.copy("*", src=os.path.join(QTSRC, d), dst=d)

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))
