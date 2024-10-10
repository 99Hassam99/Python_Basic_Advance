"""
pip install>>>desired framework


in cmd write python -m pytest or py.test or pytest -v

it goes by the prefix be sure that the file name start or end with test_ \ _test

pytest -v -rxs ( to check the reason of skipping)

use pytest -k multiply for a specific function to be tested

use pytest -m mac -v (to check functions with same name)

we can also run reverse test like run all test except mac
pytest -m "not mac" -v
"""


import mathlib
import pytest
# import sys
# @pytest.mark.skip(reason="dont need")
# def test_calc_total():
#     total = mathlib.calc_total(4,5)
#     assert total == 9
#
#
# # @pytest.mark.skipif(sys.version_info>(3,2),reason="Hy i don't need it")
# def test_calc_multiply():
#     result = mathlib.calc_multiply(10,3)
#     assert result == 30

# custom tag , this could be anyname(xyz), to test functions with same name
# # @pytest.mark.windows
# def test_windows_1():
#     assert True
# # @pytest.mark.windows
# def test_windows_2():
#     assert True
# # @pytest.mark.mac
# def test_mac_1():
#     assert True
# # @pytest.mark.mac
# def test_mac_2():
#     assert True