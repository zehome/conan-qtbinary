#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os
import shutil


qtmodule_options = (
    'qt3d', 'qtactiveqt',
    'qtandroidextras', 'qtbase', 'qtcanvas3d', 'qtcharts', 'qtconnectivity', 'qtdatavis3d',
    'qtdeclarative', 'qtdoc', 'qtgamepad', 'qtgraphicaleffects', 'qtimageformats',
    'qtlocation', 'qtmacextras', 'qtmultimedia', 'qtnetworkauth', 'qtpurchasing',
    'qtqa', 'qtquickcontrols', 'qtquickcontrols2', 'qtremoteobjects', 'qtrepotools',
    'qtscript', 'qtscxml', 'qtsensors', 'qtserialbus', 'qtserialport', 'qtspeech',
    'qtsvg', 'qttools', 'qttranslations', 'qtvirtualkeyboard', 'qtwayland', 'qtwebchannel',
    'qtwebengine', 'qtwebglplugin', 'qtwebsockets', 'qtwebview', 'qtwinextras', 'qtx11extras',
    'qtxmlpatterns',
)


class QtBinaryConan(ConanFile):
    name = "qt"
    version = "5.12.0"
    description = "Qt binary distributed by Qt company"
    topics = "conan", "qt"
    url = "https://github.com/zehome/conan-qtbinary"
    homepage = "https://www.qt.io/"
    author = "Laurent Coustet <ed@zehome.com>"
    license = "GPL-3.0-only"
    generators = "txt"
    settings = "os", "compiler", "build_type", "arch"
    build_requires = (
        "OpenSSL/1.0.2q@conan/stable",
    )

    default_options = (
        "OpenSSL:shared=True",
    )
    keep_imports = True

    options = dict({
        "shared": [True, False],
        "commercial": [True, False],
        "opengl": ["no", "es2", "desktop", "dynamic"],
        "openssl": [True, False],
        "GUI": [True, False],
        "widgets": [True, False],
        "config": "ANY",
    }, **{opt: [True, False] for opt in qtmodule_options})
    default_options = dict({
        "shared": True,
        "commercial": False,
        "opengl": "desktop",
        "openssl": False,
        "GUI": True,
        "widgets": True,
        "config": None,
    }, **{opt: False for opt in qtmodule_options}
    )
    def package(self):
        QTSRC = self.env["QT_DIR"]
        for d in ("bin", "include", "lib", "libexec",
            "mkspecs", "phrasebooks", "plugins", "qml",
            "qtvirtualkeyboard", "resources", "translations"
        ):
            self.copy("*", src=os.path.join(QTSRC, d), dst=d)

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))

    def imports(self):
        self.copy("*", src="bin", dst="bin", root_package="OpenSSL")