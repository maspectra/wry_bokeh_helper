import pytest
import pywry


def test_sum_as_string():
    assert pywry.sum_as_string(1, 1) == "2"
