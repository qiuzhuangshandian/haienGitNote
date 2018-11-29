import numpy as np
from src.config import num_steps,testSetPath,trainSetPath,mean_std
import random
from mxnet import nd



def TrainSetIter(batchSize = 5):
    trainData = np.load(trainSetPath)
    meanStd = np.load(mean_std)
    Xs = trainData["arr_0"]    # npz files use the arr_0, arr_1 ..... as the key
    Ys = trainData["arr_1"]
    # print(type(Xs))
    mean_x = meanStd["arr_0"]
    mean_y = meanStd["arr_1"]
    std = meanStd["arr_2"]
    m,_ = Ys.shape
    indexList = list(range(m))
    random.shuffle(indexList)

    for i in range(0,m,batchSize):
        if i+batchSize <= m-1:
            indecs = indexList[i:i+batchSize]
            # print(indecs)
            X = Xs[indecs]
            X = (X-mean_x)/std
            Y = Ys[indecs]
            Y -= mean_y
            # print("Y:",Y)
            yield nd.array(X),nd.array(Y)

def TestSetReader(testdata,labels,batchSize = 1,numSteps = 5):
    m,n,l = testdata.shape
    # print("m:",m,"n:",n)
    indexList = list(range(m))
    # random.shuffle(indexList)

    subIndexList = [indexList[i:i + batchSize] for i in range(0, m, batchSize)]

    for indecs in subIndexList:
        if len(indecs) == batchSize:
            # x,y = [],[]
            # for index in indecs:
            #     x_tmp = testdata[index:index+numSteps]
            #     y_tmp = labels[index:index+numSteps]
            #     x.append(x_tmp)
            #     y.append(y_tmp)
            x,y = testdata[indecs],labels[indecs]
            x,y = nd.array(x), nd.array(y)
            # print("*"*50)
            # print(indecs)
            # print(nd.transpose(x,axes=[1,0,2]))
            # print(y.T.reshape((-1,)))
            # print("*" * 50)
            yield x,y


if __name__=="__main__":
    iter = TrainSetIter()
    for x,y in iter:
        pass