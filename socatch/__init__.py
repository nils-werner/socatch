from __future__ import absolute_import
import webbrowser


def open(type, value):
    webbrowser.open(
        "https://stackoverflow.com/search?q=[python] %s: %s" %
        (type.__name__, value)
    )


def catch(e, reraise=False):
    open(type(e), str(e))
    if reraise:
        raise e
