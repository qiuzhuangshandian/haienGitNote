import json
import numpy as np
import os
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
import matplotlib.pyplot as plt

setting1 = 1 # 4
setting2 = 1 # 8
num_trees = 30
DataPath = "C:\\Users\john\Desktop\september\RNN_gas_640\data1"
# save_path = 'tfrecord_files/'
gas_label = {'GCO': [0, 0, 0, 1], 'GEa': [0, 0, 1, 0], 'GEy': [0, 1, 0, 0], 'GMe': [1, 0, 0, 0]}
gas_label_ = {'GCO': 0, 'GEa': 1, 'GEy': 2, 'GMe': 3}
units = {'B1':[],'B2':[],'B3':[],'B4':[],'B5':[]}
startPoint = 5700
dic = {}
dic['B1'] = {'R1': [], 'R2': [], 'R3': [], 'R4': [], }
dic['B2'] = {'R1': [], 'R2': [], 'R3': [], 'R4': [], }
dic['B3'] = {'R1': [], 'R2': [], 'R3': [], 'R4': [], }
dic['B4'] = {'R1': [], 'R2': []}
dic['B5'] = {'R1': [], 'R2': []}

file_list = os.listdir(DataPath)
for filename in file_list:
    name_split = filename.split('_')
    Bn = name_split[0]
    Rn = name_split[-1].split('.')[0]
    dic[Bn][Rn].append(filename)

def getDataFromFile(filename,Size,step):
    file = os.path.join(DataPath,filename)
    pf = pd.read_csv(file,header=None,sep='\t',)
    tmp = pf.values[startPoint:startPoint+Size:step,1:].T
    tmp_mean = np.mean(tmp,axis=1)
    out = (tmp-np.repeat(tmp_mean,repeats=np.shape(tmp)[1],axis=0).reshape(np.shape(tmp))).reshape([-1,])
    label =get_label(filename)
    return out, label

def get_label(name):
    ID = name.split('_')[1]
    label = gas_label_[ID]
    return label
def getBoardAccuracySetting1(Bn,step):
    train_data = []
    train_label = []
    for i, item in enumerate(dic[Bn]['R1']):
        print('\r{}:{}/{}'.format(Bn,i + 1, len(dic[Bn]['R1'])), end=" ")
        x, y = getDataFromFile(item, 400, step)
        train_data.append(x)
        train_label.append(y)
    clf = GradientBoostingClassifier(n_estimators=num_trees, learning_rate=0.1, random_state=0)
    clf.fit(train_data, train_label)
    test_data_B1R2, test_data_B1R3, test_data_B1R4 = [], [], []
    train_label_B1R2, train_label_B1R3, train_label_B1R4 = [], [], []
    if Bn in ['B4','B5']:
        for item in dic[Bn]['R2']:
            x, y = getDataFromFile(item, 400, step)
            test_data_B1R2.append(x)
            train_label_B1R2.append(y)
        acc_BnR2 = clf.score(test_data_B1R2, train_label_B1R2)
        acc_BnR3 = 0
        acc_BnR4 = 0
    else:
        for item in dic[Bn]['R2']:
            x, y = getDataFromFile(item, 400, step)
            test_data_B1R2.append(x)
            train_label_B1R2.append(y)
        for item in dic[Bn]['R3']:
            x, y = getDataFromFile(item, 400, step)
            test_data_B1R3.append(x)
            train_label_B1R3.append(y)
        for item in dic[Bn]['R4']:
            x, y = getDataFromFile(item, 400, step)
            test_data_B1R4.append(x)
            train_label_B1R4.append(y)
        acc_BnR2 = clf.score(test_data_B1R2, train_label_B1R2)
        acc_BnR3 = clf.score(test_data_B1R3, train_label_B1R3)
        acc_BnR4 = clf.score(test_data_B1R4, train_label_B1R4)
    print('\n')
    return [acc_BnR2,acc_BnR3,acc_BnR4]
def getBoardAccuracySetting2(Bn,step):
    RList = ['R1','R2','R3','R4']
    acc = []
    if Bn in ['B4','B5']:
        loop_Rn = ['R1']
    else:
        loop_Rn = ['R1','R2','R3']
    for i,Rn in enumerate(loop_Rn):
        print("{} Repeat:".format(Bn)+Rn)
        train_data = []
        train_label = []
        for j, item in enumerate(dic[Bn][Rn]):
            # print('\r{}:{}/{}'.format(Bn, j + 1, len(dic[Bn]['R1'])), end=" ")
            x, y = getDataFromFile(item, 400, step)
            train_data.append(x)
            train_label.append(y)
        clf = GradientBoostingClassifier(n_estimators=num_trees, learning_rate=0.1, random_state=0)
        clf.fit(train_data, train_label)
        test_data = []
        test_label = []
        for j, item in enumerate(dic[Bn][RList[i+1]]):
            # print('\r{}:{}/{}'.format(Bn, j + 1, len(dic[Bn]['R1'])), end=" ")
            x, y = getDataFromFile(item, 400, step)
            test_data.append(x)
            test_label.append(y)
        acc_tmp = clf.score(test_data,test_label)
        acc.append(acc_tmp)
    if Bn in ['B4', 'B5']:
          acc = acc+[0,0]
    return acc

def main():
    cwd = os.getcwd()
    print(cwd)

    # setting1
    if setting1:
        picSaveSetting1 = "C:\\Users\john\Desktop\Paper\DrawForPaper\pictures\DriftComparationGTB\setting1\\"
        print("Drift experinment setting1")
        steps = range(4, 5)
        for step in steps:
            # B1
            x = [2, 3, 4]
            fig = plt.figure()
            ax = fig.add_subplot(111)
            acc_B1 = getBoardAccuracySetting1('B1',step)
            #B2
            acc_B2 = getBoardAccuracySetting1('B2', step)
            # B3
            acc_B3 = getBoardAccuracySetting1('B3', step)
            # B4
            acc_B4 = getBoardAccuracySetting1('B4', step)
            # B5
            acc_B5 = getBoardAccuracySetting1('B5', step)

            acc1 = [acc_B1, acc_B2, acc_B3, acc_B4, acc_B5]

            ax.plot(x, acc_B1,marker='o')
            ax.plot(x, acc_B2,marker='o')
            ax.plot(x, acc_B3,marker='o')
            ax.plot(x, acc_B4,marker='o')
            ax.plot(x, acc_B5,marker='o')
            plt.title(str(step)+' '+"setting1")
            plt.savefig(picSaveSetting1+str(step)+'.png')
            plt.close()


    # setting2
    if setting2:
        picSaveSetting1 = "C:\\Users\john\Desktop\Paper\DrawForPaper\pictures\DriftComparationGTB\setting2\\"
        print("Drift experinment setting2")
        steps = range(8, 9)
        for step in steps:
            acc_B1 = getBoardAccuracySetting2('B1', step)
            acc_B2 = getBoardAccuracySetting2('B2', step)
            acc_B3 = getBoardAccuracySetting2('B3', step)
            acc_B4 = getBoardAccuracySetting2('B4', step)
            acc_B5 = getBoardAccuracySetting2('B5', step)

            acc2 = [acc_B1, acc_B2, acc_B3, acc_B4, acc_B5]

            x = [1, 2, 3]
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.plot(x, acc_B1,marker='o')
            ax.plot(x, acc_B2,marker='o')
            ax.plot(x, acc_B3,marker='o')
            ax.plot(x, acc_B4,marker='o')
            ax.plot(x, acc_B5,marker='o')
            plt.title(str(step) + ' ' + "setting2")
            plt.savefig(picSaveSetting1 + str(step) + '.png')
            plt.close()

        acc = {'setting1': acc1, 'setting2': acc2}
        print(type(acc))
        json_path = "C:\\Users\john\Desktop\Paper\DrawForPaper\Data\Comparation\DriftGTB.json"
        with open(json_path, 'w') as f:
            json.dump(acc, f)

    print('OK')

if __name__=="__main__":
    main()






