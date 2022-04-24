import platform
import sys
import numpy
import scipy
import os
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier
import pandas as pd
from joblib import dump
from sklearn import preprocessing

print(platform.platform())

print("Python", sys.version)

print("NumPy", numpy.__version__)

print("SciPy", scipy.__version__)


def train():
    print("loading data")
    data = pd.read_csv("data/immo_data.csv", nrows=10000, lineterminator='\n')
    print(data.head(1))
    print("training model")


if __name__ == '__main__':
    train()
