import sys
import pathlib

from unittest import (
    mock,
)

sys.path.append(
    str(pathlib.Path(__file__).parent.parent)
)

from resty import resty


def test_model():
    print(resty)
    assert True
