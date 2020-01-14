#!/usr/bin/env python3

# imports csv file
import csv

# checks miles driven for the valid number
def get_miles_driven():
    while True:
        miles_driven = float(input("Distance:\t"))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue

# checks gallons used for the valid number
def get_gallons_used():
    while True:
        gallons_used = float(input("Gallons:\t"))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue

def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()

        # rounds mpg
        mpg = round((miles_driven / gallons_used), 2)
        print("MPG:\t\t" + str(mpg))
        print()

        # list for data
        data_list = [["Distance", "Gallons", "MPG"]]
        data_list.append([miles_driven, gallons_used, mpg])

        # gets the data from the CSV file
        with open("trips.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data_list)

        for trip in data_list:
            print(trip[0], "\t", trip[1], "\t", trip[2])

        more = input("More entries? (y or n): ")

    print("Bye")

if __name__ == "__main__":
    main()
