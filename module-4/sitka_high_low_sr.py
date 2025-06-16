# Stephanie Ramos
# June 15, 2025
# Module 4.2 Assignment
# High\Low Temperatures

# The purpose of this code change is to update to allow user selection of high or low temperatures and loop until exit.

import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

# Menu loop
while True:
    print("\nMenu Options:")
    print("1. View High Temperatures")
    print("2. View Low Temperatures")
    print("3. Exit")
    choice = input ("Please make your selection: ")

    if choice == '3':
        print("Exiting. Thank you for using the program.")
        sys.exit()

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates and high temperatures from this file.
        dates, temps = [], []

        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
        
                if choice == '1':
                    temp = int(row[5])
                elif choice == '2':
                    temp = int(row[6])
                else:
                    print("Invalid choice. Please enter 1-3.")
                    temps = None
                    break

                dates.append(current_date)
                temps.append(temp)
            except ValueError:
                continue
    if temps:
        fig, ax=plt.subplots()
        color = 'red' if choice == '1' else 'blue' 
        label = "Highs" if choice == '1' else "Lows"

        ax.plot(dates, temps, c=color)

        # Format plot.
        plt.title(f"Daily {label} - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()