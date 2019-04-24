import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from scipy.signal import savgol_filter
import numpy as np
import csv, sys

#use csv file name as an argument
InputFile = sys.argv[1]
Ts, Pack0, Core0, Core1, Core0_fr, Core1_fr, Core2_fr, Core3_fr = [], [], [], [], [], [], [], []

with open(InputFile, mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        Ts.insert(line_count, int(row["ts"]))
        Pack0.insert(line_count, float(row["Package-id-0"].strip()))
        Core0.insert(line_count, float(row["Core-0-temp"].strip()))
        Core1.insert(line_count, float(row["Core-1-temp"].strip()))
        Core0_fr.insert(line_count, float(row["Thread-0-freq"].strip()))
        Core1_fr.insert(line_count, float(row["Thread-1-freq"].strip()))
        Core2_fr.insert(line_count, float(row["Thread-2-freq"].strip()))
        Core3_fr.insert(line_count, float(row["Thread-3-freq"].strip()))
        #print(f'\t{row["ts"]} - {row["Time"]} - {row["temp1"]} - {row["temp2"].strip()} - {row["Package id 0"].strip()} - {row["Core 0"].strip()} - {row["Core 1"].strip()}')
        line_count += 1
    print(f'Processed {line_count} lines.')

#with plt.xkcd():
# Convert to the correct format for matplotlib.
# mdate.epoch2num converts epoch timestamps to the right format for matplotlib
Secs = mdate.epoch2num(Ts)

#filter volatile data
Core0_mean = savgol_filter(Core0, 51, 1)
Core1_mean = savgol_filter(Core1, 51, 1)
Core0_fr_mean = savgol_filter(Core0_fr, 51, 1)
Core1_fr_mean = savgol_filter(Core1_fr, 51, 1)
Core2_fr_mean = savgol_filter(Core2_fr, 51, 1)
Core3_fr_mean = savgol_filter(Core3_fr, 51, 1)

#plot it
plt.figure(1)

ax = plt.subplot(211)
ax.plot(Secs, Core0, alpha=0.3, label="Core 0")
ax.plot(Secs, Core0_mean, alpha=1.0, label="Core 0 av")
ax.plot(Secs, Core1, alpha=0.3, label="Core 1")
ax.plot(Secs, Core1_mean, alpha=1.0, label="Core 1 av")
ax.set_title("Temperature log")
#ax.set_xlabel("Time")
ax.set_ylabel("Temp °C")
ax.grid(True)
ax.legend(loc="upper left")

ax.xaxis.set_major_formatter(mdate.DateFormatter("%d-%m-%y %H:%M:%S"))
ax.xaxis.set_major_locator(mdate.MinuteLocator(interval=5))
#plt.figure(1).autofmt_xdate()

bx = plt.subplot(212)
bx.plot(Secs, Core0_fr, alpha=0.1, label="Core 0")
bx.plot(Secs, Core0_fr_mean, alpha=0.8, label="Core 0 av")
bx.plot(Secs, Core1_fr, alpha=0.1, label="Core 1")
bx.plot(Secs, Core1_fr_mean, alpha=0.8, label="Core 1 av")
bx.plot(Secs, Core2_fr, alpha=0.1, label="Core 2")
bx.plot(Secs, Core2_fr_mean, alpha=0.8, label="Core 2 av")
bx.plot(Secs, Core3_fr, alpha=0.1, label="Core 3")
bx.plot(Secs, Core3_fr_mean, alpha=0.8, label="Core 3 av")
bx.set_title("Cores frequency log")
#bx.set_xlabel("Time")
bx.set_ylabel("MHz")
bx.grid(True)
bx.legend(loc="upper left")

bx.xaxis.set_major_formatter(mdate.DateFormatter("%d-%m-%y %H:%M:%S"))
bx.xaxis.set_major_locator(mdate.MinuteLocator(interval=5))

plt.figure(1).autofmt_xdate()
plt.show()