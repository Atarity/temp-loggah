import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import csv, sys

#use csv file name as an argument
InputFile = sys.argv[1]
Ts, Pack0, Core0, Core1 = [], [], [], []

with open(InputFile, mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        Ts.insert(line_count, int(row["ts"]))
        Pack0.insert(line_count, float(row["Package id 0"].strip()))
        Core0.insert(line_count, float(row["Core 0"].strip()))
        Core1.insert(line_count, float(row["Core 1"].strip()))
        #print(f'\t{row["ts"]} - {row["Time"]} - {row["temp1"]} - {row["temp2"].strip()} - {row["Package id 0"].strip()} - {row["Core 0"].strip()} - {row["Core 1"].strip()}')
        line_count += 1
    print(f'Processed {line_count} lines.')

#with plt.xkcd():
# Convert to the correct format for matplotlib.
# mdate.epoch2num converts epoch timestamps to the right format for matplotlib
Secs = mdate.epoch2num(Ts)

fig, ax = plt.subplots()
#ax.plot(Secs, Pack0, alpha=0.8, label="Package 0")
ax.plot(Secs, Core0, alpha=0.8, label="Core 0")
ax.plot(Secs, Core1, alpha=0.8, label="Core 1")
ax.set_title("Temperature log")
ax.set_xlabel("Time")
ax.set_ylabel("Temp °C")
ax.grid(True)

# Use a DateFormatter to set the data to the correct format.
ax.xaxis.set_major_formatter(mdate.DateFormatter("%d-%m-%y %H:%M:%S"))
ax.xaxis.set_major_locator(mdate.MinuteLocator(interval=5))
# Sets the tick labels diagonal so they fit easier.
fig.autofmt_xdate()

plt.legend()
plt.show()