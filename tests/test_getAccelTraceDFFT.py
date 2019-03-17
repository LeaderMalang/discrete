import unittest
import os
from main import getAccelTraceDFFT
import numpy as np

class TestGetAccelTraceDFFT(unittest.TestCase):
  def setUp(self):
    super(TestGetAccelTraceDFFT, self).setUp()
    byteFile = open('./test_dfft.dat', 'w+b')
    values = np.ndarray((5), dtype=np.float, buffer=np.array([1.1,2.2,3.3,4.4,8.8]))
    values.tofile(byteFile)
    byteFile.close()

  def tearDown(self):
    os.remove('./test_dfft.dat')

  def test_reads_values_from_file(self):
    transformedValues = getAccelTraceDFFT('./test_dfft.dat')
    assert len(transformedValues) == 5
  
  def test_handles_nonexistent_file(self):
    transformedValues = getAccelTraceDFFT('./some_file.dat')
    assert len(transformedValues) == 0

if __name__ == '__main__':
    unittest.main()
