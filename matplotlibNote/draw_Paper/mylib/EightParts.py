import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib

DataPath = "E:/papers/for_journal/may_target/codes/data1"
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
    NameList = os.listdir(DataPath)
    # *******参数配置*******
    index = 90
    sensor = 4
    start = 5800
    Range = range(start,start+400)
    cutSize = 50
    # ********参数配置******
    print(NameList[index])
    draw(NameList[index],sensor,Range,cutSize)
    plt.show()
def draw(fileName,n,Range,CutSize):
    file = os.path.join(DataPath,fileName)
    # *****************准备数据******************
    pf = pd.read_csv(file,sep='\t',header=None)
    drawData = pf.values[Range,n]
    X = pf[0].values[Range]
    drawParts(X, drawData, Range, removemean=False)
    drawParts(X,drawData,Range,removemean = True)
def drawParts(X,drawData,Range,removemean = True):
    parts = len(Range) / 50
    # *************创建绘图*********************
    pic = plt.figure(figsize=[8, 7])
    ax = pic.add_subplot(111)
    # *************四条边线宽度******************
    ax.spines['left'].set_linewidth(2.5)
    ax.spines['bottom'].set_linewidth(2.5)
    ax.spines['right'].set_linewidth(2.5)
    ax.spines['top'].set_linewidth(2.5)
    # ************刻度属性**************
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    space = np.linspace(Range[0], Range[-1], 9) - Range[0]
    c = 'g'
    for i in range(int(parts)):
        # x = X[int(round(space[i])): int(round(space[i + 1]))]

        data = drawData[int(round(space[i])): int(round(space[i + 1]))]
        x = np.linspace(start=0 + i * 0.5, stop=0 + (i + 1) * 0.5, num=len(data))
        if removemean == True:
            data = data - np.mean(data)
        ax.plot(x, data, linewidth=2.5)
        ax.axvline(x[0], linestyle='--', c=c)  # 图中竖线位置在此调整
    ax.axvline(x[-1], linestyle='--', c=c)  # 图中竖线位置在此调整
    if removemean == True:
        ax.hlines(0, 0, 4,linestyles = "dashed")

    plt.xlabel("Time(s)", fontdict=font)
    plt.ylabel(r"R(KΩ)", fontdict=font)




if __name__=="__main__":
    main()