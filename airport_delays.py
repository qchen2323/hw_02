import json
import numpy as np
import matplotlib.pyplot as plt

total_airports=[]
with open('data/Monthly Airline Delays by Airport, 2003-2016.json','r') as f:
    data_airports = json.loads(f.read())
    total_airports += data_airports

data_pts= len(total_airports)

delayed_count={} 
for year in [2003, 2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]:
    delayed_count[year]=0
for airport in total_airports:
    year = airport['Time']['Year']
    delayed_occur = airport['Statistics']['Flights']['Delayed']
    delayed_count[int(year)] += delayed_occur

on_time_count={} 
for year in [2003, 2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]:
    on_time_count[year]=0
for airport in total_airports:
    year = airport['Time']['Year']
    on_time_occur = airport['Statistics']['Flights']['On Time']
    on_time_count[int(year)] += on_time_occur

# graphing
x1 = delayed_count.keys()
y1 = delayed_count.values()
plt.plot(x1, y1, label = "Delayed",color='red', marker='s', markersize=5)
x2 = on_time_count.keys()
y2 = on_time_count.values()
plt.plot(x2, y2, label = "On-time",color='green', marker='s', markersize=5)
plt.xlabel('Year')
plt.ylabel('Number of Flights')
plt.title('Number of On-time and Delayed Flights in the US from 2003-2016')
plt.axis(xmin=2003, xmax=2016, ymin=0, ymax=4000000)
plt.xticks(np.arange(2003,2017,1))
plt.yticks(np.arange(0,4000000,250000))
plt.legend(loc='upper right',prop={'size':10})
plt.ticklabel_format(useOffset=False, style='plain')
plt.tick_params(axis='x', which='major', labelsize=10)
plt.show()