import csv
from datetime import datetime
import os
import matplotlib.pyplot as plt

os.chdir("C:/Users/robma/Desktop/Python/data_visualization")  # Change to file path.


filename = "data/sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(
        reader
    )  # next() is called only once to get the first line of the file, which contains the file headers.
    # print(header_row)

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
print(highs)

# Plot the high and low temperatures.
plt.style.use("bmh")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Format plot.
plt.title("Daily high and low temperatures - 2018\nSikta, Alaska", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()  # Draws the date labels diagonally to prevent them from overlapping.
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
