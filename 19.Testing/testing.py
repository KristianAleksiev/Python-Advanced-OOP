"""
1. Testing
- Validates that each unit of the software performs as designed
- Manual, automated

2. Unit testing
- Individual units tested, coding phase

3. Unit testing basics

4. Unit testing framework - unittest
- self.assertEqual
- self.assertTrue
- self.assertListEqual
- self.assertCountEqual
...
Triple A - Arrange, Act, Assert

Unit tests structure usually follows the structure of the code
python -m unittest folder/*.py

5. Mocking
- Making a replica of something
- How do we want something to behave in particular test
- Isolate logic
- Simulate behavior
@patch() decorator
"""

"""
Template
import unittest


class WorkerTests(unittest.TestCase):



if __name__ == "__main__":
    unittest.main()
"""