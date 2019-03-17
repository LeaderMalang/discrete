import os
import numpy as np
from config import config
import logging

logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.INFO)

complexType = np.csingle if config["inputBytesPerValue"] == "4" else np.complex64
floatType = np.float32 if config["inputBytesPerValue"] == "4" else np.float64

'''
Reads values from an input file and calculates and returns
the discrete fast fourier transform of the values
'''
def getAccelTraceDFFT(inputfile):
  try:
    accelTrace = np.fromfile(inputfile, dtype=float)
  except:
    return np.ndarray((0), dtype=np.complex, buffer=np.array([]))
  dffTAccelTrace = np.fft.fft(accelTrace)
  return dffTAccelTrace

'''
Calculates and returns mean of given array of values
'''
def getMean(values):
  return np.mean(values, None, complexType)

'''
Calculates and returns median of given array of values
'''
def getMedian(values):
  return np.median(values)

'''
Calculates and returns standard deviation of given array of values
'''
def getStandardDeviation(values):
  return np.std(values, None, complexType)

'''
Logs mean, median and standard deviation of given array of values to stdout
'''
def logStatistics(values):
  logging.info('Mean - %s', getMean(values))
  logging.info('Median - %s', getMedian(values))
  logging.info('Standard Deviation - %s', getStandardDeviation(values))

'''
Writes given array of values to output file specified in config
'''
def writeValuesToFile(values):
  outputfile = open(config["outputfile"], "w+b")
  values.tofile(outputfile)
  outputfile.close()

if __name__ == "__main__":
  dffTAccelTrace = getAccelTraceDFFT(config['inputfile'])
  logStatistics(dffTAccelTrace)
  writeValuesToFile(dffTAccelTrace)
