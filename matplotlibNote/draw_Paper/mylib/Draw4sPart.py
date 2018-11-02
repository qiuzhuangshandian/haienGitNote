import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib
DataPath = "C:\\Users\john\Desktop\september\RNN_gas_640\data1/"
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
    Range = range(5800,6200)
    # ********参数配置******
    print(NameList[index])
    draw(NameList[index],sensor,Range)

def draw(fileName,n,Range):
    file = os.path.join(DataPath,fileName)
    pf = pd.read_csv(file,sep='\t',header=None)
    drawData = pf.values[Range,n]
    x = pf[0].values[Range]
    pic = plt.figure(figsize=[8,7])
    ax = pic.add_subplot(111)
    # *************四条边线宽度******************
    ax.spines['left'].set_linewidth(2.5)
    ax.spines['bottom'].set_linewidth(2.5)
    ax.spines['right'].set_linewidth(2.5)
    ax.spines['top'].set_linewidth(2.5)
    # ************刻度属性**************
    plt.xticks(fontsize=24)
    plt.yticks(fontsize=24)
    ax.plot(x,drawData,linewidth=2.5)
    ax.axvline(58.00, linestyle='--', c='red')  # 图中竖线位置在此调整
    ax.axvline(58.50, linestyle='--', c='red')  # 图中竖线位置在此调整
    ax.axvline(59.00, linestyle='--', c='red')  # 图中竖线位置在此调整
    ax.axvline(59.50, linestyle='--', c='red')  # 图中竖线位置在此调整
    ax.axvline(60.00, linestyle='--', c='red')  # 图中竖线位置在此调整
    ax.axvline(60.50, linestyle='--', c='red')  # 图中竖线位置在此调整
    ax.axvline(61.00, linestyle='--', c='red')  # 图中竖线位置在此调整
    ax.axvline(61.50, linestyle='--', c='red')  # 图中竖线位置在此调整
    ax.axvline(62.00, linestyle='--', c='red')  # 图中竖线位置在此调整
    # #*************************绘制小箭头********************
    # ax.annotate("",(62.00,5),(58.00,5),fontsize=15,
    #                             arrowprops=dict(
    #                             arrowstyle='<|-|>',
    #                             shrinkA=0,
    #                             shrinkB=0,
    #                             fc="k", ec="k",
    #                             connectionstyle="arc3,rad=-0.05",))
    # ax.text(59.0,5.05,s='$\Delta{t}$',fontdict={
    #                     'color': 'black',
    #                     'weight': 'bold',
    #                     'size': 15,
    #                         })
    # ******************************************************
    plt.xlabel("Time(s)", fontdict=font)
    plt.ylabel(r"R(KΩ)", fontdict=font)

    plt.show()



if __name__=="__main__":
    main()