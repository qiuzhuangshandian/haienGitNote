import xlrd
import numpy as np
import random
from mxnet import nd
try:
    xlsFile = xlrd.open_workbook("E:/孙阳阳/data/dataSet.xls",'r')
    print(xlsFile.sheet_names())
except:
    print("open file error!")
table = xlsFile.sheets()[0]
nrows,ncols = table.nrows,table.ncols
print("rows:{},cols:{}".format(nrows,ncols))

data = []
headers = table.row_values(0)

for i in range(1,nrows):
    data.append(table.row_values(i)[1:17])

data = np.array(data)
std = np.std(data,axis=0)
np.save("std.npy",std)
mean = np.mean(data,axis=0)
np.save("mean.npy",mean)
data -= mean
data[:,1:] = data[:,1:]/std[1:]
# print(data)


def TrainSetIter(batchSize = 5,numSteps = 5):
    m,n = data.shape
    # print("m:",m,"n:",n)
    indexList = list(range(m-numSteps))
    random.shuffle(indexList)

    subIndexList = [indexList[i:i+batchSize] for i in range(0,len(indexList),batchSize)]
    for indecs in subIndexList:
        if len(indecs) == batchSize:
            x,y = [],[]
            for index in indecs:
                x_tmp = data[index:index+numSteps]
                y_tmp = data[index+1:index+numSteps+1,0]
                x.append(x_tmp)
                y.append(y_tmp)
            x,y = nd.array(x), nd.array(y)
            # print("*"*50)
            # print(indecs)
            # print(nd.transpose(x,axes=[1,0,2]))
            # print(y.T.reshape((-1,)))
            # print("*" * 50)
            yield x,y
def TestSetIter(testdata,batchSize = 1,numSteps = 5):
    m,n = testdata.shape
    # print("m:",m,"n:",n)
    indexList = list(range(m-numSteps))
    # random.shuffle(indexList)

    subIndexList = [indexList[i:i+batchSize] for i in range(0,len(indexList),batchSize)]
    for indecs in subIndexList:
        if len(indecs) == batchSize:
            x,y = [],[]
            for index in indecs:
                x_tmp = testdata[index:index+numSteps]
                y_tmp = testdata[index+1:index+numSteps+1,0]
                x.append(x_tmp)
                y.append(y_tmp)
            x,y = nd.array(x), nd.array(y)
            # print("*"*50)
            # print(indecs)
            # print(nd.transpose(x,axes=[1,0,2]))
            # print(y.T.reshape((-1,)))
            # print("*" * 50)
            yield x,y


if __name__=="__main__":
    iter = TrainSetIter(2,3)
    print(iter)
    for x,y in iter:
        pass
        # print(x)
        # print(y)
