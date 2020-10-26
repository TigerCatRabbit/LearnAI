import sys,time

for i in range(1,101):
    print('\rhello',end=' ') 
    print("\r下载进度：%.2f%%" %(float(i/100*100)),end=' ') 
    time.sleep(0.01) 
print()
for i in range(1,101):
    print('\rhello',end=' ') 
    print("\r下载进度：%.2f%%" %(float(i/100*100)),end=' ') 
    time.sleep(0.01) 
    # print("\r下载：%.2f%%" %(float(i/100*100)),end=' ') 
# for i in range(10000):
#     print('shuchushuliang:',end='')
