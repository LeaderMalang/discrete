import os
import configparser

configP = configparser.ConfigParser()
configP.read('./config.ini')

config = {
  "inputfile": os.getenv('INPUT_FILE', configP.get('inputsettings', 'inputfile')),
  "inputSampleRate": os.getenv('INPUT_SAMPLE_RATE', configP.get('inputsettings', 'inputSampleRate')),
  "inputBytesPerValue": os.getenv('INPUT_BYTES_PER_VALUE', configP.get('inputsettings', 'inputBytesPerValue')),
  "outputfile": os.getenv('OUTPUT_FILE', configP.get('outputsettings', 'outputfile')),
  "outputSampleRate": os.getenv('OUTPUT_SAMPLE_RATE', configP.get('outputsettings', 'outputSampleRate')),
  "outputBytesPerValue": os.getenv('OUTPUT_BYTES_PER_VALUE', configP.get('outputsettings', 'outputBytesPerValue'))
}

