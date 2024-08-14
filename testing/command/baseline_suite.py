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