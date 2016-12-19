'''
Created on Dec 18, 2016

@author: DucTruong
'''
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import linear_model
from sklearn import tree
import pickle

# data = pd.read_csv('finalDataStatistic.csv')
# data = data.loc[data['commentCount'] != -1]
# data = data.sample(frac=1).reset_index(drop=True)
# save_dataset = open('./pickle/trainingTestingData_2.pickle', 'wb')
# pickle.dump(data, save_dataset)
# save_dataset.close();
open_file = open("./pickle/trainingTestingData_2.pickle", "rb")
data = pickle.load(open_file)
open_file.close()
#print(data)
training_set, testing_set = train_test_split(data, test_size=0.15)
saveData = open('./pickle/training_set.pickle', 'wb')
pickle.dump(training_set, saveData)
saveData.close();

saveData = open('./pickle/testing_set.pickle', 'wb')
pickle.dump(testing_set, saveData)
saveData.close();

#print(training_set, testing_set)
# training_X = training_set[['descriptioncount','descriptionsentiment','tagcount','tagsentiment','duration','categoryId']]
# training_Y = training_set[['viewCount']]
# testing_X = testing_set[['descriptioncount','descriptionsentiment','tagcount','tagsentiment','duration','categoryId']]
# testing_Y = testing_set[['viewCount']]
training_X = training_set[['duration','categoryId']]
training_Y = training_set[['viewCount']]
testing_X = testing_set[['duration','categoryId']]
testing_Y = testing_set[['viewCount']]

clf = linear_model.BayesianRidge()
clf2 = linear_model.LinearRegression()
clf3 = linear_model.LogisticRegression()
clf4 = linear_model.Lasso()
clf5 = tree.DecisionTreeRegressor()
clf6 = linear_model.ElasticNet()

clf.fit(training_X,training_Y)
# result = clf.predict(testing_X)
print("BayesianRidge Model Accuracy: ", clf.score(testing_X, testing_Y))
save_classifier = open('./pickle/BayesianRidge.pickle', 'wb')
pickle.dump(clf, save_classifier)
save_classifier.close();

clf2.fit(training_X,training_Y)
# result = clf2.predict(testing_X)
print("LinearRegression Model Accuracy: ", clf2.score(testing_X, testing_Y))
save_classifier = open('./pickle/LinearRegression.pickle', 'wb')
pickle.dump(clf2, save_classifier)
save_classifier.close();

# clf3.fit(training_X,training_Y)
# # result = clf3.predict(testing_X)
# print("LogisticRegression Model Accuracy: ", clf3.score(testing_X, testing_Y))
# save_classifier = open('./pickle/LogisticRegression.pickle', 'wb')
# pickle.dump(clf3, save_classifier)
# save_classifier.close();

clf4.fit(training_X,training_Y)
# result = clf4.predict(testing_X)
print("Lasso Model Accuracy: ", clf4.score(testing_X, testing_Y))
save_classifier = open('./pickle/Lasso.pickle', 'wb')
pickle.dump(clf4, save_classifier)
save_classifier.close();

clf5.fit(training_X,training_Y)
# result = clf5.predict(testing_X)
print("DecisionTreeRegressor Model Accuracy: ", clf5.score(testing_X, testing_Y))
save_classifier = open('./pickle/DecisionTreeRegressor.pickle', 'wb')
pickle.dump(clf5, save_classifier)
save_classifier.close();

clf6.fit(training_X,training_Y)
# result = clf5.predict(testing_X)
print("ElasticNet Model Accuracy: ", clf6.score(testing_X, testing_Y))
save_classifier = open('./pickle/ElasticNet.pickle', 'wb')
pickle.dump(clf6, save_classifier)
save_classifier.close();