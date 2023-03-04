import pytest
from pydevops.flip import flipper

def test_reverse():
    assert flipper('this') == "siht"