# import os, sys
# os.chdir(sys.path[0])


file='00.txt'
txtf=open(file,'a+')
for i in range(10):
    txtf.write(str(i))
txtf.close()
with open("test.txt","w") as f:
    f.write("这是个测试！")  # 自带文件关闭功能，不需要再写f.close()