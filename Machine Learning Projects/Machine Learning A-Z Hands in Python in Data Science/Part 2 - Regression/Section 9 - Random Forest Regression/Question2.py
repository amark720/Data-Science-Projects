# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 20:38:55 2018

@author: MY
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values