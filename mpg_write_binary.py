#!/usr/bin/env python3
# Slav Chmut
# 1/16/20

# imports csv file
import pickle

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

        for trips in data_list:
            print(trips[0], "\t", trips[1], "\t", trips[2])

        # gets the data from the CSV file
        with open("trips.bin", "wb") as file:
            pickle.dump(trips, file)

        # reads 
        with open("trips.bin", "rb") as file:
            data_list = pickle.load(file)

        more = input("More entries? (y or n): ")
        print()

    print("Bye")

if __name__ == "__main__":
    main()
