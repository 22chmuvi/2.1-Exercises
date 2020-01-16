#!/usr/bin/env python3
# Slav Chmut
# 1/16/20

import os
import pickle

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
def dump_trips(data_list):
    with open("trips.bin", "wb") as file:
        pickle.dump(dump_trips, file)

# read the data from the trips.csv file
def load_trips():
    target = "trips.bin"
    if os.path.getsize(target) > 0:
        with open(target, "rb") as file:
            data_list = pickle.load(file)

def list_trips(data_list):
    for trips in data_list:
        print(trips[0], "\t", trips[1], "\t", trips[2])

def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    load_trips()

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

        dump_trips(data_list)

        more = input("More entries? (y or n): ")
        print()

    print("Bye")

if __name__ == "__main__":
    main()
