"""
1.problem with this code is writing same code again and again
2.This can be done easy or can be done in one function by passing paramter
"""

import mathlib
import pytest
from parametarize_mathlib import calc_square
# 2 solution
@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (5,25),
                             (10,100),
                             (2,4),
                             (9,81)
                         ]
                         )
def test_calc_square(test_input, expected_output):
    result = mathlib.calc_square(test_input)
    assert result == expected_output

# 1 problem
# def test_calc_square_2():
#     result = mathlib.calc_square(10)
#     assert result == 100
#
#
# def test_calc_square_3():
#     result = mathlib.calc_square(2)
#     assert result == 4
#
#
# def test_calc_square_4():
#     result = mathlib.calc_square(9)
#     assert result == 81