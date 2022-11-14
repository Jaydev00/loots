import os
import sys
for inputFile in os.listdir(sys.argv[1]):
    os.rename(sys.argv[1] + inputFile, sys.argv[1] + inputFile.lower())