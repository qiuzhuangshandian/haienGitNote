import csv
import matplotlib.pyplot as plt

shaixuan = 1
if shaixuan == 1:
    preFile = "lstmpreValue_shai1.csv"
    lossFile = "loss_shai1.csv"
    svmPreFile = "SvmPreValue_shai1.csv"

else:
    preFile = "lstmpreValue.csv"
    lossFile = "loss.csv"
    svmPreFile = "SvmPreValue.csv"
def readCsv(file):
    data = []
    with open(file) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        birth_header = next(csv_reader)  # 读取第一行每一列的标题
        for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
            data.append(row)

    def string_to_float(stringList):
        tmp = []
        for item in stringList:
            tmp.append(float(item))
        return tmp

    data = list(map(string_to_float,data))
    return data

f = lambda x:(x[0]-x[1])**2
s = 0
e = []
data = readCsv(preFile)
for item in data:
    e.append(f(item))
    s += f(item)
MSE = s/len(data)
print("the mean square error of lstm based rnn model is:[{}]".format(MSE))
figure1 = plt.figure()
ax1 = figure1.add_subplot(111)
ax1.plot(range(len(data)),[tmp[0] for tmp in data ],"-o",c="r",label="Predict")
ax1.plot(range(len(data)),[tmp[1] for tmp in data],"-*",c = "b",label = "True")
plt.xlabel("number")
plt.ylabel("value")
plt.title("rnn pre and true")
plt.legend()

figure3 = plt.figure()
ax1 = figure3.add_subplot(111)
ax1.plot(range(len(data)),e,"-o",label = "error")
e_mean = [sum(e)/len(e)]*len(e)
ax1.plot(range(len(data)),e_mean,"-*",label = "average")
plt.xlabel("number")
plt.ylabel("single MSE value and MES line")
plt.title("rnn mse")
plt.legend()

lossData = readCsv(lossFile)
figure2 = plt.figure()
ax2 = figure2.add_subplot(111)
ax2.plot([tmp[0] for tmp in lossData[:200]],[tmp[1] for tmp in lossData[:200]])
plt.xlabel("opoch")
plt.ylabel("loss value")
plt.title("rnn loss")


###############svm part######################
s = 0
e = []
data = readCsv(svmPreFile)
for item in data:
    e.append(f(item))
    s += f(item)
MSE = s/len(data)
print("the mean square error of  SVM model is:[{}]".format(MSE))
svmfigure1 = plt.figure()
ax1 = svmfigure1.add_subplot(111)
ax1.plot(range(len(data)),[tmp[0] for tmp in data ],"-o",c="r",label="Predict")
ax1.plot(range(len(data)),[tmp[1] for tmp in data],"-*",c = "b",label = "True")
plt.xlabel("number")
plt.ylabel("value")
plt.title("svm pre and true value")
plt.legend()

svmfigure2 = plt.figure()
ax1 = svmfigure2.add_subplot(111)
ax1.plot(range(len(data)),e,"-o",label = "error")
e_mean = [sum(e)/len(e)]*len(e)
ax1.plot(range(len(data)),e_mean,"-*",label = "average")
plt.xlabel("number")
plt.ylabel("single MSE value and MES line")
plt.title("svm mse")
plt.legend()

plt.show()