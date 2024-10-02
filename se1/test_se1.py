import sys
import os
import helpers
import pytest

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

import se1

MODULE = "se1"

@pytest.mark.parametrize("a,x,expected", [(2, 3, 64), (3, 2, 25), 
                                          (4, 0, 1), (0, 4, 16) ])
def test_add_two_and_raise(a,x, expected):
    """Test add_two_and_raise"""
    recreate_msg = helpers.gen_recreate_msg(MODULE, "add_two_and_raise", a, x)

    try:
        actual = se1.add_two_and_raise(a, x)
    except Exception as e:  # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

@pytest.mark.parametrize("a,b,expected", [(2, 3, True), (3, -2, False), 
                                          (-4, -1, True), (-10, 4, False) ])
def test_same_sign(a,b,expected):
    """Test same_sign"""
    recreate_msg = helpers.gen_recreate_msg(MODULE, "same_sign", a, b)

    try:
        actual = se1.same_sign(a, b)
    except Exception as e:  # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("x,expected", [(2, "EVEN"), (3, "ODD"), 
                                        (0, "EVEN"), (4, "EVEN") ])
def test_num_to_parity(x, expected):
    """Test num_to_parity"""
    recreate_msg = helpers.gen_recreate_msg(MODULE, "num_to_parity", x)

    try:
        actual = se1.num_to_parity(x)
    except Exception as e: # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

@pytest.mark.parametrize("a,b,expected", [(12, 18, 4), (3, 5, 1), 
                                          (4, 4, 3), (1, 1, 1) ])
def test_num_common_divisors(a,b,expected):
    """Test num_common_divisors"""
    recreate_msg = helpers.gen_recreate_msg(MODULE, "num_common_divisors", a, b)

    try:
        actual = se1.num_common_divisors(a, b)
    except Exception as e:  # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e) 

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("lst,expected", [
    ([1,2,3,-1], "POSITIVES"), 
    ([1,2,3], "POSITIVES"), 
    ([1,2,3,-1,0], "POSITIVES"), 
    ([1,2,3,-1,0,-2], "POSITIVES"), 
    ([0], "NEITHER"), 
    ([-1,-2,-3], "NEGATIVES"), 
    ([-1,-2,-3,0], "NEGATIVES"), 
    ([-1,-2,-3,0,1], "NEGATIVES")])
def test_count_negatives_positives(lst, expected):
    """Test count_negatives_positives"""
    recreate_msg = helpers.gen_recreate_msg(MODULE, "count_negatives_positives", lst)

    lst_copy = lst.copy()

    try:
        actual = se1.count_negatives_positives(lst)
    except Exception as e: # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)

    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    # Check that the original list was not modified
    err_msg = helpers.check_list_unmodified("lst", lst, lst_copy)
    if err_msg is not None:
        pytest.fail(err_msg)


@pytest.mark.parametrize("lst,x,expected", [
    ([1,2,3,4,5,6], 2, [2,4,6]),
    ([1,2,3,4,5,6], 3, [3,6]),
    ([1,2,3,4,5,6,7,8,9,10], 5, [5,10]),
    ([1,2,3,4,5,6,7,8,9,10], 1, [1,2,3,4,5,6,7,8,9,10]),
])
def test_keep_if_multiple(lst, x, expected):
    """Test keep_if_multiple"""
    recreate_msg = helpers.gen_recreate_msg(MODULE, "keep_if_multiple", lst, x)

    lst_copy = lst.copy()

    try:
        actual = se1.keep_if_multiple(lst, x)
    except Exception as e: # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    # Check that the original list was not modified
    err_msg = helpers.check_list_unmodified("lst", lst, lst_copy)
    if err_msg is not None:
        pytest.fail(err_msg)

    