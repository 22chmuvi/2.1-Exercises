#!/usr/bin/env python3
# Slav Chmut
# 1/16/20

import csv

def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :     "))
        if miles_driven > 0:
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue

def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:    "))
        if gallons_used > 0:
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue

# writes the data from a two-dimensional list named data_list
def write_trips(data_list):
    with open("trips.csv", "w+", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data_list)

# read the data from the trips.csv file
def read_trips():
    with open("trips.csv", newline="") as file:
        reader = csv.reader(file)
        for trip in reader:
            print(trip[0], "\t", trip[1], "\t", trip[2])

def list_trips(data_list):
    for trip in data_list:
        print(trip[0], "\t", trip[1], "\t", trip[2])

def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    read_trips()

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()

        # rounds mpg
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:\t " + str(mpg))
        print()

        data_list = [["Distance", "Gallons", "MPG"]]
        data_list.append([miles_driven, gallons_used, mpg])

        write_trips(data_list)

        more = input("More entries? (y or n): ")

    print("Bye")

if __name__ == "__main__":
    main()
