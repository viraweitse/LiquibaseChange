# test_liquibasechange.py
"""
Tests for LiquibaseChange module.
"""

import unittest
from liquibasechange import LiquibaseChange

class TestLiquibaseChange(unittest.TestCase):
    """Test cases for LiquibaseChange class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LiquibaseChange()
        self.assertIsInstance(instance, LiquibaseChange)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LiquibaseChange()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
