Conan Qt binary repackage
=========================

Repackages Qt binary to a "qtbinary" conan package.

You must install Qt binary form and specify **QT_DIR** in the [env] of the
profile you use to build this package.

Example profile:
```
[settings]
os=Windows
os_build=Windows
arch=x86_64
arch_build=x86_64
compiler=Visual Studio
compiler.version=15
build_type=Release
[options]
[build_requires]
[env]
QT_DIR=E:\Qt\5.11.2\msvc2017_64
```
