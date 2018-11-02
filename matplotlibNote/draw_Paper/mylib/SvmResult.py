import numpy as np
import pandas as pd
from sklearn.svm import SVC
import os,time,json
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt

# 取step = 18 作为对比
DataPath = "E:/papers/for_journal/may_target/codes/data1"
picSavePath = "E:/papers/for_journal/may_target/codes/DrawForPaper/pictures/comparationSVM"
jsonPath ="E:/papers/for_journal/may_target/codes/DrawForPaper/Data/Comparation"
startPoint = 5700
cutLength = [50,100,150,200,250,300,350,400]
# step = 17
gas_label_ = {'GCO': 0, 'GEa': 1, 'GEy': 2, 'GMe': 3}
K = 10  # the number of folder for cross validation
def get_all_files(path):
    return os.listdir(path)

def get_label(name):
    ID = name.split('_')[1]
    label = gas_label_[ID]
    return label

def getDataFromFile(filename,Size,step):
    file = os.path.join(DataPath,filename)
    pf = pd.read_csv(file,header=None,sep='\t',)
    tmp = pf.values[startPoint:startPoint+Size:step,1:].T
    tmp_mean = np.mean(tmp,axis=1)
    # print(np.repeat(tmp_mean,repeats=np.shape(tmp)[1],axis=0).reshape(np.shape(tmp)))
    out = (tmp-np.repeat(tmp_mean,repeats=np.shape(tmp)[1],axis=0).reshape(np.shape(tmp))).reshape([-1,])
    # print(np.shape(out))
    label =get_label(filename)
    # return tmp.reshape([-1,]), label
    return out, label

def main():
    print(time.asctime(time.localtime(time.time())))
    fileList = get_all_files(DataPath)

    t = [0.5,1,1.5,2,2.5,3,3.5,4]

    for step in range(17,18):
        print("step = %d"%step)
        fig = plt.figure()
        acc_c = []
        for size in cutLength:
            X_set = []
            Y_set = []
            for i,file in enumerate(fileList):
                print("\r{}/{}".format(i,len(fileList)),end=" ")
                x,y = getDataFromFile(file,size,step)
                X_set.append(x)
                Y_set.append(y)
                # print(np.array(Y_set).reshape([-1,1]))
            X_set = np.array(X_set)
            Y_set = np.array(Y_set)
            # print(X_set)
            kf = KFold(n_splits=K)
            acc_s = []
            for trainIndex, testIndex in kf.split(X_set):
                train_data,train_label = [X_set[i] for i in trainIndex],[Y_set[i] for i in trainIndex]
                test_data,test_label = [X_set[i] for i in testIndex],[Y_set[i] for i in testIndex]
                # print(test_label)
                clf = SVC(C=100, kernel='rbf', degree=3, gamma=0.001,
                          coef0=0.0, shrinking=True, probability=False,
                          tol=0.001, cache_size=200, class_weight=None, verbose=False,
                          max_iter=-1, decision_function_shape='ovr', random_state=None)
                clf.fit(train_data, train_label)
                acc = clf.score(test_data, test_label)
                acc_s.append(acc)
            print(acc_s,np.mean(acc_s))
            acc_c.append(np.mean(acc_s))
        acc_save = {"acc": acc_c}
        with open(jsonPath + "SVMacc.json", 'w') as f:
            json.dump(acc_save, f)
        plt.plot(t,acc_c)
        plt.title(str(step))
        plt.savefig(picSavePath+"/"+str(step)+".png")
    # plt.show()
    print("OK!")
if __name__=="__main__":
    main()