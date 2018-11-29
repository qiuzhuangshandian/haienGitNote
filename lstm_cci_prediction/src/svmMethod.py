from sklearn import svm
import numpy as np
from src.config import trainSetPath,testSetPath,mean_std,svmPredictValuePath
import csv

meanStd = np.load(mean_std)
mean_x = meanStd["arr_0"]
mean_y = meanStd["arr_1"]
std = meanStd["arr_2"]

trainSet = np.load(trainSetPath)
testSet = np.load(testSetPath)

Xs = trainSet["arr_0"] - mean_x
Ys = trainSet["arr_1"] - mean_y

m,h,l = Xs.shape
Xs = np.reshape(Xs,[m,-1])
Ys = Ys[:,-1]

testXs = testSet["arr_0"] - mean_x
testYs = testSet["arr_1"]

m_test,h_test,l_test = testXs.shape
testXs = np.reshape(testXs,[m_test,-1])
testYs = testYs[:,-1] - mean_y

clf = svm.SVR(kernel='rbf', C=1e7, gamma=1e-10)
# clf = svm.SVR(kernel='linear', C=1000)
# clf = svm.SVR(kernel='poly', C=1000,gamma=0.1)
clf.fit(Xs, Ys)


# print(testXs)
# print(testXs.shape)
pre = clf.predict(testXs)
np.set_printoptions(precision=2)
pre_s = pre+mean_y
testY_s = testYs+mean_y
# print(pre_s)
# print(testY_s)
print(np.mean((pre_s-testY_s)**2))

fw = open(svmPredictValuePath,"w",newline = "")
csvWriter = csv.writer(fw,dialect="excel")
csvWriter.writerow(["predict value","true value"])
for pre_,testY_ in zip(pre_s.tolist(),testY_s.tolist()):
    csvWriter.writerow([pre_,testY_])
fw.close()
