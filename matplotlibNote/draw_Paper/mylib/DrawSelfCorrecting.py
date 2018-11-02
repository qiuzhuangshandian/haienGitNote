import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import matplotlib

# analysisPath = "C:\\Users\john\Desktop\January\DrawForPaper\Data\AnalysisSaved\\"
analysisPath = "E:/papers/for_journal/may_target/codes/DrawForPaper/Data/AnalysisSaved/"

# ************
withmean = 0
# ************
if withmean:
    SubDataPath = "WithMeanSelfCorrecting"
    picPath = "E:/papers/for_journal/may_target/codes/DrawForPaper/pictures/withmeanselCorrect"
    jsonPath = "E:\papers/for_journal\may_target\codes\DrawForPaper\Data\Comparation\withmeanCrnnAcc.json"
else:
    SubDataPath = "selfCorrecting"
    picPath = "E:/papers/for_journal/may_target/codes/DrawForPaper/pictures/selfCorrect"
    jsonPath = "E:\papers/for_journal\may_target\codes\DrawForPaper\Data\Comparation\crnnAcc.json"
K = 10
font = {'family': 'serif',
                'color': 'black',
                'weight': 'bold',
                'size': 20
        }
'''set the direction of the ticks
'''
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
def main():
    t = [0.5,1,1.5,2,2.5,3,3.5,4]
    tmp = []
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    ax.spines['left'].set_linewidth(2.5)
    ax.spines['bottom'].set_linewidth(2.5)
    ax.spines['right'].set_linewidth(2.5)
    ax.spines['top'].set_linewidth(2.5)
    for i in range(K):
        pf = pd.read_csv(analysisPath+SubDataPath+"/cross"+str(i)+"_acc.csv")
        ax.plot(t, pf.values[0,:]*100,marker = "o")
        tmp.append(pf.values[0,:])
    # plt.title("10 fold cross validation")
    ax.set_yticks(range(70, 101, 5))
    plt.ylabel(r"Accuracy(%)", fontdict=font)
    plt.xlabel("Time(s)", fontdict=font)
    plt.savefig(picPath + "CrossAcc.png")
    plt.savefig(picPath + "singleCrossAcc.png")
    y = np.mean(np.array(tmp),0)*100
    with open(jsonPath,'w') as f:
        y_save = {"acc":list(y)}
        json.dump(y_save,f)
    print("*" * 50)
    print(y)
    print("*" * 50)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    ax.spines['left'].set_linewidth(2.5)
    ax.spines['bottom'].set_linewidth(2.5)
    ax.spines['right'].set_linewidth(2.5)
    ax.spines['top'].set_linewidth(2.5)
    ax.plot(t,y,marker = "o",linewidth=2.5)
    ax.set_yticks(range(82, 101, 2))
    plt.xlabel("Time(s)", fontdict=font)
    plt.ylabel(r"Accuracy(%)", fontdict=font)
    plt.savefig(picPath+"CrossAcc.png")
    plt.show()
if __name__=="__main__":
    main()