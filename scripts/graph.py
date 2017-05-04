import csv
import matplotlib.pyplot as plt
import os
import matplotlib.dates as md
import dateutil

times=[]
concentrations=[]
latitudes=[]
longitudes=[]
nums=[]
i = 0;
with open('../data/log.csv','r') as csvFile:
    reader=csv.reader(csvFile,delimiter=',')
    next(reader)
    num = 0
    for row in reader:
        i += 1
        nums.append(i)
        temp=row[0]
        times.append(temp)
        temp=row[2]
        concentrations.append(temp)
        temp=row[3]
        latitudes.append(temp)
        temp=row[4]
        longitudes.append(temp)

# plt.plot(nums, concentrations)
# plt.show()

dates = [dateutil.parser.parse(s) for s in times]

plt.subplots_adjust(bottom=0.2)
plt.xticks( rotation=25 )

ax=plt.gca()
# ax.set_xticks(dates)

xfmt = md.DateFormatter('%H:%M:%S')
ax.xaxis.set_major_formatter(xfmt)

plt.plot(dates, concentrations)
plt.show()
