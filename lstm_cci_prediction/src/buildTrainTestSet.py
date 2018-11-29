
import csv,xlrd,random
import numpy as np
from config import num_steps,test_VS_train,testSetPath,trainSetPath,mean_std,raw_data_path,featureNumber,TrainTestIndexPath
import json
try:
    xlsFile = xlrd.open_workbook(raw_data_path,'r')
    print(xlsFile.sheet_names())
except:
    print("open file error!")
table = xlsFile.sheets()[0]
nrows,ncols = table.nrows,table.ncols
print("*"*50)
print("row and cols of raw file: rows:{},cols:{}".format(nrows,ncols))
headers = table.row_values(0)
print("header of raw file:",headers)
data = []
for i in range(1,nrows):
    data.append(table.row_values(i)[1:featureNumber+1])

data = np.array(data)
m,n = data.shape
print("The shape of total data set:[{},{}]".format(m,n))
print("*"*50)

# indexList = list(range(m-num_steps))
# random.shuffle(indexList)
# TestIndexList = [indexList[i] for i in range(int(m*test_VS_train))]
# TrainIndexList = list(set(indexList) - set(TestIndexList))
with open(TrainTestIndexPath,"r") as fr:
    indexDict = json.load(fr)
TrainIndexList = indexDict["train"]
TestIndexList = indexDict["test"]
x,y = [],[]

indexRecord_x,indexRecord_y = [],[]
for index in TrainIndexList:
    indexRecord_x.extend(range(index,index + num_steps))
    x_tmp = data[index:index + num_steps]
    indexRecord_y.extend(range(index+1, index + num_steps+1))
    y_tmp = data[index + 1:index + num_steps + 1, 0]
    x.append(x_tmp)
    y.append(y_tmp)
x,y = np.array(x),np.array(y)
np.savez(trainSetPath,x,y)

indexRecord_x,indexRecord_y = list(set(indexRecord_x)),list(set(indexRecord_y))
mean_x = np.mean(data[indexRecord_x],axis=0)
mean_y = np.mean(data[indexRecord_y,0],axis=0)
std = np.std(data[indexRecord_x],axis=0)
# print(std)
np.savez(mean_std,mean_x,(mean_y+mean_x[0])/2,std)

x,y = [],[]
for index in TestIndexList:
    x_tmp = data[index:index + num_steps]
    y_tmp = data[index + 1:index + num_steps + 1, 0]
    x.append(x_tmp)
    y.append(y_tmp)
x,y = np.array(x),np.array(y)

np.savez(testSetPath,x,y)
print("train and test set are built ok! \nand has been saved in the dir:[{}],\n[{}].".format(trainSetPath,testSetPath))






