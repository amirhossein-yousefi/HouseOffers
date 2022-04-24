import platform
import sys
import numpy
import scipy
import os
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier
import pandas as pd
from joblib import load
from sklearn import preprocessing

print(platform.platform())

print("Python", sys.version)

print("NumPy", numpy.__version__)

print("SciPy", scipy.__version__)

def inference():
    print("running tests ...")


if __name__ == '__main__':
    inference()