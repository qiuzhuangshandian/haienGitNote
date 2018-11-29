
shaixuan = 1
###################lstm part######################
#model structure
num_steps = 5
if not shaixuan:
    featureNumber = 17     # number of feature
else:
    featureNumber = 8     # number of feature
num_hiddens = 50
num_outputs = 1       #only predict one value

##########data set#################
if not shaixuan:
    raw_data_path = "E:/孙阳阳/data/数据改.xls"    #modify the path of raw xls file
    test_VS_train = 1/5                          # modify the Proportion of test and train set
    testSetPath = "E:/孙阳阳/data/testSet.npz"    # modify your dir
    trainSetPath = "E:/孙阳阳/data/trainSet.npz"  # modify your dir

    mean_std = "E:/孙阳阳/data/meanstd.npz"



else:
    ##shai xuan
    raw_data_path = "E:/孙阳阳/data/筛选指标的数据.xls"    #modify the path of raw xls file
    test_VS_train = 1/5                          # modify the Proportion of test and train set
    testSetPath = "E:/孙阳阳/data/testSet_shai1.npz"    # modify your dir
    trainSetPath = "E:/孙阳阳/data/trainSet_shai1.npz"  # modify your dir

    mean_std = "E:/孙阳阳/data/meanstd_shai1.npz"
TrainTestIndexPath = "E:/孙阳阳/src/splitIndex.json"
##############model save##################
if not shaixuan:
    paramPath = "./params.param"

##shai xuan
else:
    paramPath = "./params_shai1.param"
##############train hyperparams#################
num_epochs = 200
lr = 0.1
clipping_theta = 0.1
batch_size = 10
pred_period = 5
momentum = 0.95

#record for plot
if not shaixuan:
    lossPath = "E:/孙阳阳/record/loss.csv"
    predictValuePath = "E:/孙阳阳/record/lstmpreValue.csv"
#shai xuan
else:
    lossPath = "E:/孙阳阳/record/loss_shai1.csv"
    predictValuePath = "E:/孙阳阳/record/lstmpreValue_shai1.csv"
#########################################################
#######################svm part##################################
if not shaixuan:
    svmPredictValuePath = "E:/孙阳阳/record/SvmPreValue.csv"

#shai xuan
else:
    svmPredictValuePath = "E:/孙阳阳/record/SvmPreValue_shai1.csv"





#####################################################