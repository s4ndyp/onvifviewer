# SPDX-FileCopyrightText: Casper Meijn <casper@meijn.net>
#
# SPDX-License-Identifier: CC0-1.0

import info
from Package.CMakePackageBase import *


class subinfo(info.infoclass):
    def setTargets(self):
        self.displayName = "ONVIFViewer"
        self.description = "View and control network cameras using the ONVIF protocol"
        self.webpage = "https://gitlab.com/caspermeijn/onvifviewer"
        self.svnTargets["master"] = "https://github.com/s4ndyp/onvifviewer.git"
        self.defaultTarget = "master"

    def setDependencies(self):
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.buildDependencies["libs/gettext"] = None
        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/qt/qtbase"] = None
        self.runtimeDependencies["libs/qt/qtdeclarative"] = None
        self.runtimeDependencies["libs/qt/qtsvg"] = None
        self.runtimeDependencies["libs/qt/qtxml"] = None
        self.runtimeDependencies["libs/qt5/qtquickcontrols2"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kcoreaddons"] = None
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kirigami"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kxmlgui"] = None
        self.runtimeDependencies["qt-libs/kdsoap"] = None
        self.runtimeDependencies["qt-libs/kdsoap-ws-discovery-client"] = None
        self.runtimeDependencies["kde/plasma/breeze"] = None
        self.runtimeDependencies["kde/frameworks/tier1/breeze-icons"] = None
        self.runtimeDependencies["kde/frameworks/tier3/qqc2-desktop-style"] = None


class Package(CMakePackageBase):
    def __init__(self):
        super().__init__()
        self.subinfo.options.configure.args += ["-DBUILD_TESTING=OFF"]

    def createPackage(self):
        self.defines["executable"] = r"bin\onvifviewer.exe"
        self.defines["icon_png"] = self.sourceDir() / "desktop/ApplicationIcon-256.png"
        self.defines["icon_png_44"] = self.sourceDir() / "desktop/ApplicationIcon-48.png"
        self.blacklist_file.append(self.blueprintDir() / "blacklist.txt")
        self.addExecutableFilter(r"(bin)/(?!(onvifviewer)\.exe$).*")
        self.ignoredPackages.append("binary/mysql")
        if not CraftCore.compiler.isLinux:
            self.ignoredPackages.append("libs/dbus")
        return super().createPackage()
