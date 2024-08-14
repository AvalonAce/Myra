import unittest

from testing.command.baseline_suite import *

# Testing Suite ---------------------------------------
# This is the high-level function that will run all testing functions.
# Testing functions should be split into files in separate directories.
# Configure the this file and testing files as neccesary.
# -----------------------------------------------------

def run_test_suite():
    # Build the test suite
    suite = unittest.TestSuite()
    
    # Add testing classes and functions here
    # Format is as follows: addTest(TestClass('test_function'))
    suite.addTest(TestBaselineSuite('test_baseline_suite'))
    
    # Run the test suite
    return unittest.TextTestRunner(verbosity=2).run(suite)