from __future__ import absolute_import
import sys

from .__init__ import open


oldexcepthook = sys.excepthook


def socatchhook(type, value, traceback):
    open(type, value)
    oldexcepthook(type, value, traceback)

sys.excepthook = socatchhook
