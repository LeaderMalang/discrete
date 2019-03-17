import unittest
import random
from main import getMean

class TestGetMean(unittest.TestCase):
  def setUp(self):
    super(TestGetMean, self).setUp()

  def test_calculates_mean(self):
    intarray = [random.randint(0,10) for e in range(10)]
    assert str(getMean(intarray).real) == str(sum(intarray)/len(intarray))

if __name__ == '__main__':
    unittest.main()
