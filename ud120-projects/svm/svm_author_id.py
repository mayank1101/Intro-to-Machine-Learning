#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# clf = SVC(kernel='linear')
clf = SVC(kernel='rbf', C=10000.0) # setting C = 10000.0 gives accuracy of 99.8%

# Training and predicting only on 1% of data
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

t0 = time()
clf.fit(features_train, labels_train)
print("Training Time:", round(time()-t0, 3), "s")

t0 = time()
pred = clf.predict(features_test)
print('Test Time:', round(time()-t0, 3), "s")

print('Prediction for data point 10 ',pred[10])
print('Prediction for data point 26 ', pred[26])
print('Prediction for data point 10 ', pred[50])
print('Number of mails classified as chris ',np.count_nonzero(pred == 1))
print(accuracy_score(labels_test, pred))
#########################################################


