# test_nimbusyarn.py
"""
Tests for NimbusYarn module.
"""

import unittest
from nimbusyarn import NimbusYarn

class TestNimbusYarn(unittest.TestCase):
    """Test cases for NimbusYarn class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NimbusYarn()
        self.assertIsInstance(instance, NimbusYarn)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NimbusYarn()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
