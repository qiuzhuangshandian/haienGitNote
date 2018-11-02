import os
cwd = os.getcwd()
print(cwd)
file = os.path.join(cwd,'mylib','DriftLDAresult.py')
cmd = "python "+file
os.system(cmd)

file = os.path.join(cwd,'mylib','DriftKNNresult.py')
cmd = "python "+file
os.system(cmd)

file = os.path.join(cwd,'mylib','DriftGTBresult.py')
cmd = "python "+file
os.system(cmd)

print('over!')
