import pytest
try:
    import mock
except ImportError:
    import unittest.mock as mock
import socatch
import contextlib


@contextlib.contextmanager
def noopwith():
    yield


@mock.patch('webbrowser.open')
@pytest.mark.parametrize('reraise', [False, True])
def test_catchall(wbopen, reraise):
    with pytest.raises(Exception) if reraise else noopwith():
        try:
            raise Exception("Foo")
        except Exception as e:
            socatch.catch(e, reraise)

    wbopen.assert_called_with(
        'https://stackoverflow.com/search?q=[python] Exception: Foo'
    )
