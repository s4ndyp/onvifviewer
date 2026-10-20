# SPDX-FileCopyrightText: Casper Meijn <casper@meijn.net>
#
# SPDX-License-Identifier: CC0-1.0

import info
from Package.CMakePackageBase import *
from Utils import CraftHash


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets["master"] = "https://github.com/KDAB/KDSoap.git|kdsoap-1.10.0"
        self.targets["1.10.0"] = "https://github.com/KDAB/KDSoap/releases/download/kdsoap-1.10.0/kdsoap-1.10.0.tar.gz"
        self.targetInstSrc["1.10.0"] = "kdsoap-1.10.0"
        self.targetDigests["1.10.0"] = (
            ["0c606ecc434466dbadb2829820ca163af60cc7ca226f553b5d4032196737338f"],
            CraftHash.HashAlgorithm.SHA256,
        )

        self.defaultTarget = "1.10.0"
        self.description = "A Qt-based client-side and server-side SOAP component"
        self.webpage = "https://www.kdab.com/products/kd-soap"
        self.displayName = "KDSoap"

    def setDependencies(self):
        self.runtimeDependencies["libs/qt/qtbase"] = None


class Package(CMakePackageBase):
    def __init__(self, **args):
        super().__init__()
        self.subinfo.options.configure.args += [
            "-DKDSoap_QT6=OFF",
            "-DKDSoap_TESTS=OFF",
            "-DKDSoap_EXAMPLES=OFF",
            "-DKDSoap_DOCS=OFF",
        ]
