import pandas as pd
import json

files = [
    'E:/papers/for_journal/may_target/codes/DrawForPaper/Data/Comparation/DriftGTB.json',
    'E:/papers/for_journal/may_target/codes/DrawForPaper/Data/Comparation/DriftKNN.json',
    'E:/papers/for_journal/may_target/codes/DrawForPaper/Data/Comparation/DriftLDA.json',
    'E:/papers/for_journal/may_target/codes/DrawForPaper/Data/Comparation/DriftRF.json',
    'E:/papers/for_journal/may_target/codes/DrawForPaper/Data/Comparation/DriftSVM.json'
]

def main():
    for file in files:
        with open(file,'r') as f:
            data = json.load(f)
        acc_setting1 = data['setting1']
        acc_setting2 = data['setting2']
        for i,item in enumerate(acc_setting1):
            mean = float(sum(item)/len(item))
            if i in [0,1,2]:
                acc_setting1[i].append(mean)
            else:
                acc_setting1[i].append(item[0])

        for i,item in enumerate(acc_setting2):
            mean = float(sum(item)/len(item))
            if i in [0,1,2]:
                acc_setting2[i].append(mean)
            else:
                acc_setting2[i].append(item[0])

        columns = ['2','3','4','Average']
        pf_setting1 = pd.DataFrame(acc_setting1,columns=columns)

        columns = ['1->2','2->3','3->4','Average']
        pf_setting2 = pd.DataFrame(acc_setting2,columns=columns)

        title = file.split('\\')[-1].split('.')[0]
        print('\n')
        print('*'*25+title+'*'*25)
        print('#####setting1#####')
        print(pf_setting1)
        print('#####setting2#####')
        print(pf_setting2)
        print('*' * 50)



if __name__=="__main__":
    main()