import json
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image


savepath = 'E:/papers/for_journal/may_target/codes/DrawForPaper/DriftData/TrainSave/'
# SubSavePaths = ['12_34/','13_24/','14_23/','23_14/','24_13/','34_12/']
Units = ['B1/','B2/','B3/','B4/','B5/']
leaffolders  = ['Model/','CsvJson/','Pictures/']

def show_setting1():
    acc = []
    for unit in Units:
        with open(savepath+unit+leaffolders[1]+'bestaccuracy.json') as f:
            data = json.load(f)
            data = [data['best_accuracy']]+data['each_acc']
            while len(data) < 4:
                data.append(None)
            acc.append(data)
    acc = np.array(acc)
    acc = pd.DataFrame(acc,index = Units,columns = ['mean','2','3','4'])
    print('*' * 20, 'setting1', '*' * 19)
    print(acc)
    print('*'*49)
def show_setting2():
    savepath_2 = 'E:/papers/for_journal/may_target/codes/DrawForPaper/DriftData/TrainSave2/'
    pattern = {'B1': ['1_2', '2_3', '3_4'], 'B2': ['1_2', '2_3', '3_4'], 'B3': ['1_2', '2_3', '3_4'],
               'B4': ['1_2'], 'B5': ['1_2']
               }
    units = ['B1', 'B2', 'B3', 'B4', 'B5']
    acc = []
    for unit in units:
        acc_tmp = []
        for item in pattern[unit]:
            with open(savepath_2+unit+'/'+item+'/'+leaffolders[1]+'bestaccuracy.json') as f:
                data = json.load(f)['best_accuracy']
                # print(data)
                acc_tmp.append(data)
        average_v = float(sum(acc_tmp)) / len(acc_tmp)
        while len(acc_tmp) < 3:
            acc_tmp.append(None)
        acc_tmp.append(average_v)
        acc.append(acc_tmp)

    acc = np.array(acc)
    acc = pd.DataFrame(acc,index = Units,columns=['1->2','2->3','3->4','Average'])
    print('*'*20,'setting2','*'*19)
    print(acc)
    print('*' * 49)

def main():
    show_setting1()
    show_setting2()


if __name__=="__main__":
    main()