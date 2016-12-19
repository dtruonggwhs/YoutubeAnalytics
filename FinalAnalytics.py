'''
Created on Dec 19, 2016

@author: DucTruong
'''
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import linear_model
from sklearn import tree
import pickle
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

open_file = open("./pickle/testing_set.pickle", "rb")
testing_set = pickle.load(open_file)
open_file.close()
# testing_X = testing_set[['descriptioncount','descriptionsentiment','tagcount','tagsentiment','duration','categoryId']]
testing_X = testing_set[['duration','categoryId']]
testing_Y = testing_set[['viewCount']]

open_file = open("./pickle/training_set.pickle", "rb")
training_set = pickle.load(open_file)
open_file.close()
# training_X = training_set[['descriptioncount','descriptionsentiment','tagcount','tagsentiment','duration','categoryId']]
training_X = training_set[['duration','categoryId']]
training_Y = training_set[['viewCount']]


# open_file = open("./pickle/BayesianRidge.pickle", "rb")
# BayesianRidge = pickle.load(open_file)
# open_file.close()
# # result = BayesianRidge.predict(testing_X)
# result = cross_val_score(BayesianRidge, training_X, training_Y)
# print("BayesianRidge result: ", result)


# open_file = open("./pickle/LinearRegression.pickle", "rb")
# LinearRegression = pickle.load(open_file)
# open_file.close()
# result = cross_val_score(LinearRegression, training_X, training_Y)
# print("LinearRegression result: ", result)

# open_file = open("./pickle/LogisticRegression.pickle", "rb")
# LogisticRegression = pickle.load(open_file)
# open_file.close()
# result = cross_val_score(LogisticRegression, training_X, training_Y)
# print("LogisticRegression result: ", result)


open_file = open("./pickle/Lasso.pickle", "rb")
Lasso = pickle.load(open_file)
open_file.close()
predictionResult = Lasso.predict(testing_X)
result = cross_val_score(Lasso, training_X, training_Y)
testing_set['predicted_value'] = np.round(list(predictionResult),0)
# allParamCatLikeCountPrediction = testing_set.to_csv('durCatViewCountPrediction.csv')
print("Lasso result: ", result)
# print("Lasso result: ", pd.DataFrame(predictionResult))
# print(testing_set)


# open_file = open("./pickle/ElasticNet.pickle", "rb")
# ElasticNet = pickle.load(open_file)
# open_file.close()
# predictionResult = ElasticNet.predict(testing_X)
# result = cross_val_score(ElasticNet, training_X, training_Y)
# testing_set['predicted_value'] = list(predictionResult)
# durCatLikeCountPrediction = testing_set.to_csv('durCatLikeCountPrediction.csv')
# print("ElasticNet result: ", result)
# print("Lasso result: ", pd.DataFrame(predictionResult))
# print(testing_set)


# open_file = open("./pickle/DecisionTreeRegressor.pickle", "rb")
# DecisionTreeRegressor = pickle.load(open_file)
# open_file.close()
# result = cross_val_score(DecisionTreeRegressor, training_X, training_Y)
# print("DecisionTreeRegressor result: ", result)




