import random
import csv
import time
import os
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
if os.path.exists('zxc.csv'):
    os.remove('zxc.csv')


while True:
    f=open('zxc.csv','a',newline="")
    f_writter=csv.writer(f,delimiter=',')
    a,b=datetime.now().strftime('%H:%M:%S'),random.random()
    f_writter.writerow([a,b])
    print("Data written")
    time.sleep(1)
    f.close()
'''hrL=[]
mL=[]
secL=[]
value=[]
with open('zxc.csv','r') as f:
    csv_reader=csv.reader(f,delimiter=',')
    for row in csv_reader:
        time,val=row
        t=time.split(":")
        hr=t[0]
        m=t[1]
        sec=t[2]
        hrL.append(hr)
        mL.append(m)
        secL.append(sec)
        value.append(float(val))
timestamp=[]
for i in range(0,len(hrL)):
    timestamp.append(hrL[i]+":"+mL[i]+":"+secL[i])
plt.plot(timestamp,value)
plt.title("Sensor data")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()
#print(hrL)
#print(mL)
#print(secL)
#print(value)
#print(timestamp)'''
    
