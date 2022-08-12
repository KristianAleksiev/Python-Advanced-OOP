import unittest
from unittest import TestCase


class FirstTest(TestCase):  # Test suite
    @classmethod
    def setUpClass(cls) -> None:
        """Runs once before all tests"""

    def setUp(self) -> None:
        """Runs before each test"""
        pass

    def tearDown(self) -> None:
        """Runs after each test"""
        pass

    def test_expect_1_to_equal_1(self):  # Test case
        self.assertEqual(1, 1)

    def test_expect1_to_equal_2(self):
        self.assertEqual(1, 2)


if __name__ == "__main__":  # Test runner
    unittest.main()
