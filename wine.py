#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 11:33:36 2017

@author: koichiro
"""
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

wine = pd.read_csv('/Users/Shared/py/winequality-red.csv', sep=';')

clf = linear_model.LinearRegression()

X = wine.drop(['quality'], axis=1)

Y = wine['quality']

clf.fit(X, Y)

print(clf.coef_)
print(clf.intercept_)

print(pd.DataFrame({"Name":X.columns,
                    "Coefficients":clf.coef_}).sort_values(by='Coefficients') )
plt.matshow(wine.corr())
pd.scatter_matrix(wine)
plt.scatter(X, Y)
