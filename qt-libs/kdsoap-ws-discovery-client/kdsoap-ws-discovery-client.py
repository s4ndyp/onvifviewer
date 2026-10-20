# SPDX-FileCopyrightText: Casper Meijn <casper@meijn.net>
#
# SPDX-License-Identifier: CC0-1.0

import info
from Package.CMakePackageBase import *


class subinfo(info.infoclass):
    def setTargets(self):
        self.displayName = "KDSoap WS-Discovery Client"
        self.description = "WS-Discovery client library for KDSoap"
        self.webpage = "https://gitlab.com/caspermeijn/kdsoap-ws-discovery-client"
        self.svnTargets["master"] = "https://gitlab.com/caspermeijn/kdsoap-ws-discovery-client.git"
        self.defaultTarget = "master"

    def setDependencies(self):
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/qt/qtbase"] = None
        self.runtimeDependencies["qt-libs/kdsoap"] = None


class Package(CMakePackageBase):
    def __init__(self, **args):
        super().__init__()
        self.subinfo.options.configure.args += [
            "-DBUILD_TESTING=OFF",
            "-DBUILD_QCH=OFF",
        ]
