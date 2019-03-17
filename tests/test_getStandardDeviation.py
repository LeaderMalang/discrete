import unittest
from unittest.mock import patch
import random
from main import getStandardDeviation

class TestGeStandardDeviation(unittest.TestCase):
  def setUp(self):
    super(TestGeStandardDeviation, self).setUp()

  def test_uses_numpy_module_to_get_standard_deviation(self):
    with patch('numpy.std', return_value=[]) as verifyUsedNumpyStd:
      intarray = [random.randint(0,10) for e in range(10)]
      getStandardDeviation(intarray)
      verifyUsedNumpyStd.assert_called_once()

if __name__ == '__main__':
    unittest.main()
