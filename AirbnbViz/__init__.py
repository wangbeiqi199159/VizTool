import pandas as pd
import json
import os.path
import numpy as np 
import pandas as pd 
import sklearn
import sklearn.linear_model
import sklearn.preprocessing
from sklearn import  cross_validation
from sklearn.linear_model import  Ridge, RidgeCV, Lasso, LassoCV
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from  sklearn.feature_selection import chi2
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import  RandomizedLogisticRegression