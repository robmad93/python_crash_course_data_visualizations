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

    # Get dates and rainfall from this file.
    dates, rainfall_rate = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            rainfall = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            rainfall_rate.append(rainfall)

# Plot the rainfall.
plt.style.use("bmh")
fig, ax = plt.subplots()
ax.plot(dates, rainfall_rate, c="blue")

# Format plot.
plt.title("Daily rainfall - 2018", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()  # Draws the date labels diagonally to prevent them from overlapping.
plt.ylabel("Rainfall", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
