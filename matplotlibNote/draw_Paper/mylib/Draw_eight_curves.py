
class drawCurves(object):
    def __init__(self):
        self.dataPath = "C:\\Users\\john\\Desktop\\september\\RNN_gas_640\\data1\\"
        self.font = {'family': 'serif',
                'color': 'black',
                'weight': 'bold',
                'size': 20,
                }
        self.label = ['S1','S2','S3','S4','S5','S6','S7','S8']
        self.linecolor = ['red','blue','m','yellowgreen','g','y'
                          ,'orange','pink']
    def draw(self,name):
        import pandas as pd
        import numpy as np
        import seaborn as sns
        import matplotlib.pyplot as plt
        import matplotlib
        sns.set(style="ticks", palette="muted", color_codes=True)

        '''set the direction of the ticks
        '''
        matplotlib.rcParams['xtick.direction'] = 'in'
        matplotlib.rcParams['ytick.direction'] = 'in'

        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.xticks(fontsize=18)
        plt.yticks(fontsize=18)
        ax.spines['left'].set_linewidth(2.5)
        ax.spines['bottom'].set_linewidth(2.5)
        ax.spines['right'].set_linewidth(2.5)
        ax.spines['top'].set_linewidth(2.5)
        data = pd.read_csv(self.dataPath+name,sep='\t',header=None)
        values = data.values[:,1:]
        timeAx = data.values[:,0]
        m,n = np.shape(values)
        print(m,n)
        for i in range(n):
            drawdata = values[:,i]
            ax.plot(timeAx,drawdata,label = self.label[i],c = self.linecolor[i],
                     linewidth=1.5)
        plt.xlabel("Time(s)", fontdict=self.font)
        plt.ylabel(r"$R(KΩ)$", fontdict=self.font)
        plt.legend(loc='center left', bbox_to_anchor=(0.98, 0.75), ncol=1, fontsize = 14)
        plt.show()


def main():
    draw = drawCurves()
    draw.draw(name='B2_GEy_F040_R2.txt')





if __name__ == "__main__":
    main()