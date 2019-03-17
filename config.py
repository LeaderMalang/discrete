import os
import configparser

configP = configparser.ConfigParser()
configP.read('./config.ini')

config = {
  "inputfile": os.getenv('INPUTFILE', configP.get('inputsettings', 'inputfile')),
  "inputSampleRate": os.getenv('INPUT_SAMPLE_RATE', configP.get('inputsettings', 'inputSampleRate')),
  "inputBytesPerValue": os.getenv('INPUT_BYTES_PER_VALUE', configP.get('inputsettings', 'inputBytesPerValue')),
  "outputfile": os.getenv('OUTPUTFILE', configP.get('outputsettings', 'outputfile'))
}
