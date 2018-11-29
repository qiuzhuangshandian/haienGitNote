from mxnet import nd,cpu
from src.functions import LoadParams,PredictResult,lstm
from src.config import mean_std,testSetPath,paramPath,predictValuePath
from src.SetReader import TestSetReader

import numpy as np
import csv



num_hiddens, num_steps =  50, 5

allData = np.load(testSetPath)
TestData = allData["arr_0"]
True_y = allData["arr_1"]

meanStd = np.load(mean_std)
mean_x = meanStd["arr_0"]
mean_y = meanStd["arr_1"]
std = meanStd["arr_2"]

TestData -= mean_x
TestData = TestData/std
print(type(TestData),TestData.shape)
# True_y -= mean_y

testIter = TestSetReader(TestData,True_y,numSteps=num_steps)

modelparams = LoadParams(paramPath)

fw = open(predictValuePath, "w", newline="")
csvWriter = csv.writer(fw, dialect="excel")
csvWriter.writerow(["predict value","true value"])
for x,y in testIter:
    pre = PredictResult(X=x,rnn=lstm,batch_size=1,params=modelparams,num_hiddens=num_hiddens,ctx=cpu(0))
    print("*"*50)
    # print(x.asnumpy()*std+mean)
    print("predict value:",pre.reshape((-1,)).asnumpy()+mean_y)
    print("true value",y[0][-1].asnumpy())
    csvWriter.writerow([(pre.asnumpy()+mean_y).tolist()[0][0],y[0][-1].asnumpy().tolist()[0]])
    # preValueRecord.append([pre.asnumpy().tolist()[0][0],y[0][-1].asnumpy().tolist()[0]])
    print("*" * 50)
fw.close()
