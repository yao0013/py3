#!/usr/bin/env python

"""
Copyright (c) 2006-2021 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.data import logger
from plugins.generic.enumeration import Enumeration as GenericEnumeration

class Enumeration(GenericEnumeration):
    def getRoles(self, *args, **kwargs):
        warnMsg = "on Vertica it is not possible to enumerate the user roles"
        logger.warn(warnMsg)

        return {}
