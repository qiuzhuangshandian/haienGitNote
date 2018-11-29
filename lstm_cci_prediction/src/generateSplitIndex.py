import csv,xlrd,random
import numpy as np
from config import num_steps,test_VS_train,raw_data_path,featureNumber,TrainTestIndexPath
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

indexList = list(range(m-num_steps))
random.shuffle(indexList)
TestIndexList = [indexList[i] for i in range(int(m*test_VS_train))]
TrainIndexList = list(set(indexList) - set(TestIndexList))

saveDict = {}
with open(TrainTestIndexPath,"w") as fw:
    saveDict["train"] = TrainIndexList
    saveDict["test"] = TestIndexList
    json.dump(saveDict,fw)
print("index save ok!")