import matplotlib.pyplot as plt
import json
import numpy as np
import matplotlib
List2np = lambda x: np.array(x)


jsonPath ="E:/papers/for_journal/may_target/codes/DrawForPaper/Data/Comparation/"
t = [0.5,1,1.5,2,2.5,3,3.5,4]
font = {'family': 'serif',
        'color': 'black',
        'weight': 'bold',
        'size': 24,
        }
'''set the direction of the ticks
        '''
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
def main():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # *************四条边线宽度******************
    ax.spines['left'].set_linewidth(2.5)
    ax.spines['bottom'].set_linewidth(2.5)
    ax.spines['right'].set_linewidth(2.5)
    ax.spines['top'].set_linewidth(2.5)
    # ************刻度属性**************
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    with open(jsonPath+"crnnAcc.json") as f:
        ax.plot(t,json.load(f)['acc'],marker = 'o',label = 'CRGNN(remove the mean value)',linewidth=3.5)

    with open(jsonPath+"withmeanCrnnAcc.json") as f:
        ax.plot(t,100*List2np(json.load(f)['acc']),marker = 'o',label = 'CRGNN(keep the mean value)')
    with open(jsonPath+"rfAcc.json") as f:
        ax.plot(t,100*List2np(json.load(f)['acc']),marker = 'o',label = 'RF')
    #
    with open(jsonPath+"GTBAcc.json") as f:
        ax.plot(t,100*List2np(json.load(f)['acc']),marker = 'o',label = 'GTB')

    with open(jsonPath+"KNNAcc.json") as f:
        ax.plot(t,100*List2np(json.load(f)['acc']),marker = 'o',label = 'KNN')
    #
    with open(jsonPath+"SVMacc.json") as f:
        ax.plot(t,100*List2np(json.load(f)['acc']),marker = 'o',label = 'SVM')
    #
    with open(jsonPath+"LDAacc.json") as f:
        ax.plot(t,100*List2np(json.load(f)['acc']),marker = 'o',label = 'LDA')

    ax.legend(loc="center left",bbox_to_anchor = (0.6,0.23),ncol=1,fontsize = 14,frameon=True)
    # ax.legend(loc='center left', bbox_to_anchor=(0.99, 0.75), ncol=1, fancybox=True, shadow=True)
    ax.set_xlabel("Time (s)",fontdict=font)
    ax.set_ylabel("Accuracy(%)",fontdict=font)
    plt.show()


if __name__=="__main__":
    main()