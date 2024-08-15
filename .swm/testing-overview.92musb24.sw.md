---
title: Testing Overview
---
## Testing Framework

We use python's **unittest** for testing purposes. A structure exists to support testing in multiple files of different suites. Please follow the testing structure to implement tests.

## Testing Structure

### <SwmPath>[services/testing/TESTING.py](/services/testing/TESTING.py)</SwmPath>

This is the main testing file that runs testing suites. <SwmToken path="/services/testing/TESTING.py" pos="11:2:4" line-data="def Run_Test_Suite():">`Run_Test_Suite()`</SwmToken> is the function called in the main function which runs tests. It is a scaffold to build a suite based on any testing classes created.

To prevent any overlapping changes due to testing needs, **you should NOT commit any changes to this file.** You may commit any testing files (like <SwmPath>[services/testing/command/baseline_suite.py](/services/testing/command/baseline_suite.py)</SwmPath>) provided they are in an appropriate directory and follow named conventions.

To add tests to the prebuilt suite, use the singular baseline test in the testing file as an example.

If you wish to build your own suite(s) to call later, write them in separate files in an appropriate directory and edit this file to run them.

<SwmSnippet path="services/testing/TESTING.py" line="11">

---

Function Definition

```
def Run_Test_Suite():
    # Build the test suite
    suite = unittest.TestSuite()
    
    # Add testing classes and functions here
    # Format is as follows: addTest(TestClass('test_function'))
    suite.addTest(TestBaselineSuite('test_baseline_suite'))
    
    # Run the test suite
    return unittest.TextTestRunner(verbosity=2).run(suite)
```

---

</SwmSnippet>

### Run the tests

You can then use any of the following methods to run tests:

1. Set Myra's operating mode to "TESTING", then use in the command line:`py ENTRY.py`
2. Use python's built in command line testing found here: <https://docs.python.org/3/library/unittest.html#organizing-tests>

## Writing tests

### <SwmPath>[services/testing/command/baseline_suite.py](/services/testing/command/baseline_suite.py)</SwmPath>

In order to write a test or a suite of tests, a class must be created to house testing functions. Each class has a <SwmToken path="/services/testing/command/baseline_suite.py" pos="5:4:6" line-data="class TestBaselineSuite(unittest.TestCase):">`unittest.TestCase`</SwmToken> parameter and can have a <SwmToken path="/services/testing/command/baseline_suite.py" pos="6:3:3" line-data="    def setUp(self):">`setUp`</SwmToken>, <SwmToken path="/services/testing/command/baseline_suite.py" pos="10:3:3" line-data="    def tearDown(self):">`tearDown`</SwmToken>, or <SwmToken path="/services/testing/TESTING.py" pos="16:17:17" line-data="    # Format is as follows: addTest(TestClass(&#39;test_function&#39;))">`test_function`</SwmToken>.

The official python testing docs can be found here: <https://docs.python.org/3/library/unittest.html#organizing-tests>

<SwmSnippet path="/services/testing/command/baseline_suite.py" line="1">

---

Basic Testing File

```python
import unittest

from audio.AUDIO import Say

class TestBaselineSuite(unittest.TestCase):
    def setUp(self):
        print("\nSetting up Baseline Suite...")
        pass
    
    def tearDown(self):
        print("Tearing down Baseline Suite...")
        pass
    
    def test_baseline_suite(self):
        # Baseline Test
        Say("Test baseline suite completed!")
        self.assertTrue(True)
```

---

</SwmSnippet>

### Best Practices

When writing tests, follow a few guidelines.

- Try to test as small as possible, following unit testing practices.
- Place files you create in folders that follow the main repo structure, separating by function.
- **Again, do NOT commit changes from** <SwmPath>[services/testing/TESTING.py](/services/testing/TESTING.py)</SwmPath>**. You may edit the file to your own needs.**
- If you are testing the customized voice, be aware of your **character limit** on Elevenlabs to ensure you don't run out.

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBUENBQSUzQSUzQUF2YWxvbkFjZQ==" repo-name="PCAA"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
