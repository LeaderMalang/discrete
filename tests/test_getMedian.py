import unittest
import random
from main import getMedian

class TestGetMedian(unittest.TestCase):
  def setUp(self):
    super(TestGetMedian, self).setUp()

  def test_calculates_median(self):
    intarray = [random.randint(0,10) for e in range(3)]
    intarray.sort()
    median = intarray[int(1)]
    assert (getMedian(intarray)) == (median)

if __name__ == '__main__':
    unittest.main()
