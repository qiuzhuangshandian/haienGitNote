from mylib import EightParts as ep
from mylib import DrawOneSensorResponse as dsr
from mylib import SvmResult as  SR
from mylib import DrawSelfCorrecting as DSC
from mylib import RfResult as RFR
from mylib import GTBResult as GR
from mylib import comparations as compare
from mylib import ShowDriftResults as SDR
from mylib import ShowDriftComparationResults as SDCR

#**************配置运行的函数****************

sel = "9"    # ******* #

runFun = {
    "1":ep.main,# 画8段
    "2":dsr.main,# 画反应曲线
    "3":DSC.main,# 画交叉验证自纠正平均曲线图
    "4":SR.main, # 画SVM对比试验图
    "5":RFR.main, # 画随机森林的结果图
    "6":GR.main,  # 画梯度树提升的结果图
    "7":compare.main, # 将不同的算法的结果画在同一幅图上

    "8":SDR.main, # 显示CRNN漂移结果
    "9":SDCR.main # 显示漂移特性的对比实验结果
}
# ******************************
def main():
   runFun[sel]()



if __name__=="__main__":
    main()