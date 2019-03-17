import os
import numpy as np
from config import config
import logging

logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.INFO)

floatType = np.csingle if config["inputBytesPerValue"] == "4" else np.complex64

def getAccelTraceDFFT(inputfile):
  accelTrace = np.fromfile(inputfile)
  dffTAccelTrace = np.fft.fft(accelTrace)
  return dffTAccelTrace

def getMean(values):
  return np.mean(values, None, floatType)

def getMedian(values):
  return np.median(values)

def getStandardDeviation(values):
  return np.std(values, None, floatType)

def logStatistics(values):
  logging.info('Mean - %s', getMean(values))
  logging.info('Median - %s', getMedian(values))
  logging.info('Standard Deviation - %s', getStandardDeviation(values))

# def writeValuesToFile(values):
#   np.savetxt(config['outputfile'], values, encoding='byte')

if __name__ == "__main__":
  dffTAccelTrace = getAccelTraceDFFT(config['inputfile'])
  logStatistics(dffTAccelTrace)
  # writeValuesToFile(dffTAccelTrace)
