import sys
import os
import copy
import pytest

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

import se2
import helpers

MODULE = "se2"

@pytest.mark.parametrize("a,b,c,expected",
                         [
                             (3,4,5, True),
                             (5,12,13, True),
                             (8,15,17, True),
                             (7,24,25, True),
                             (9,40,41, True),
                             (1,2,3, False),
                             (2,3,4, False),
                             (1,1,1, False),
                             (10,11,12, False),
                         ])
def test_pythagorean_triplets(a,b,c, expected):
    """Test pythagorean_triple"""
    recreate_msg = helpers.gen_recreate_msg(MODULE, "pythagorean_triple", a, b, c)

    try:
        actual = se2.pythagorean_triple(a, b, c)
    except Exception as e:  # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("lst,expected",
                         [
                             ([1, 2, 3, 4, 5], 1),
                             ([2, 4, 5, 6, 7], 5),
                             ([2, 0, 0, 0, 4, 5], 5),
                             ([0, 0, 0, 0, 0, 0], 0),
                             ([8, 6, 4, 2, 0], 0),
                             ([], 0)
                         ])
def test_first_odd_value(lst, expected):
    """Test first_odd_value"""
    recreate_msg = helpers.gen_recreate_msg(MODULE, "first_odd_value", lst)

    try:
        actual = se2.first_odd_value(lst)
    except Exception as e:  # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)




@pytest.mark.parametrize("lst, lb, ub, expected", [
    ([], 0, 2, []),
    ([1], 0, 2, [1]),
    ([0, 1, 2], 0, 2, [0, 1, 2]),
    ([1, 4, 4, 3, -3], -2, 5, [1, 4, 4, 3, -2]),
    ([-1, 9, 0, 3, 3, 7], -2, 5, [-1, 5, 0, 3, 3, 5]),
    ([0, -1, 2, 4, -5, 7, 1], 0, 2, [0, 0, 2, 2, 0, 2, 1])
])
def test_clip_in_range(lst, lb, ub, expected):
    """Test clip_in_range"""
    recreate_msg = helpers.gen_recreate_msg(MODULE, "clip_in_range", lst,lb,ub)

    try:
        rv = se2.clip_in_range(lst,lb,ub)
        assert rv is None
    except Exception as e:  # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(lst, expected) # lst should be modified in place
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("a,b,expected", [
    (0, 1, [0, 1]),
    (1, 2, [1, 2]),
    (0, 2, [0, 1, 2]),
    (0, 6, [0, 1, 2, 3, 4, 5, 6]),
    (4, 9, [4, 5, 6, 7, 8, 9]),
    (12, 25, [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
])
def test_expand(a, b, expected):
    """Test expand"""
    recreate_msg = helpers.gen_recreate_msg(MODULE, "expand", a,b)

    try:
        actual = se2.expand(a,b)
    except Exception as e:  # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

@pytest.mark.parametrize("lst,expected", [
    ([[1,2,3],
      [4,5,6],
      [7,8,9]],
     [1,4,7,2,5,8,3,6,9]),
    ([[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12],
      [13,14,15,16]],
     [1,5,9,13,2,6,10,14,3,7,11,15,4,8,12,16]),
    ([[1,2],
      [3,4],
      [5,6],
      [7,8]],
      [1,3,5,7,2,4,6,8])
])
def test_flatten_columns(lst, expected):
    """Test flatten_columns"""
    recreate_msg = helpers.gen_recreate_msg(MODULE, "flatten_columns", lst)

    lst_copy = copy.deepcopy(lst)

    try:
        actual = se2.flatten_columns(lst)
    except Exception as e: # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


    err_msg = helpers.check_1d_iterable(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    err_msg = helpers.check_2D_list_unmodified("lst", lst_copy, lst)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
