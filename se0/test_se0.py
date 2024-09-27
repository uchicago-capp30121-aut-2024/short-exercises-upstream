import sys
import os
import helpers
import pytest

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

import se0

MODULE = "se0"

def test_two_plus_three():
    """
    Tests the two_plus_three function    
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "two_plus_three", *())
    try:
        actual = se0.two_plus_three()
    except Exception as e:  # pylint: disable=broad-except
         helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, 5)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
