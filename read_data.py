import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv
from datetime import datetime
'''hrL=[]
mL=[]
secL=[]
value=[]'''
times=[]
values=[]
with open('zxc.csv','r') as f:
    csv_reader=csv.reader(f,delimiter=',')
    for row in csv_reader:
        time,val=row
        times.append(datetime.strptime(time,"%H:%M:%S"))
        values.append(float(val))
        #print(time)
        #print(" ")
        #print(val)
        #print(type(time))
#print(times)
print(type(times[0]))
'''t=time.split(":")
        hr=t[0]
        m=t[1]
        sec=t[2]
        hrL.append(hr)
        mL.append(m)
        secL.append(sec)
        value.append(float(val))
timestamp=[]
for i in range(0,len(hrL)):
    timestamp.append(hrL[i]+":"+mL[i]+":"+secL[i])'''
plt.plot(times,values)
plt.title("Sensor data")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()
