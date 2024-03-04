#!/usr/bin/env python3
import csv

__author__ = "Mikkel Rask"
__version__ = "0.1.0"
__license__ = "MIT"


# Open the input CSV file for reading and create an output file for writing
def prepend_apostrophy_on_leading_zeros(file):
    # filename without .csv
    filename = file[:-3]
    with open(file, "r", encoding="ISO-8859-1") as input_file, open(
        filename + "parsed.csv", "w", encoding="utf-8", newline=""
    ) as output_file:
        # Create a CSV reader object
        reader = csv.reader(input_file)
        # Create a CSV writer object
        writer = csv.writer(output_file)

        # Iterate through each row in the CSV
        for row in reader:
            # Check if the first element in the row starts with '0'
            if row[0].startswith("0"):
                # If it does, prepend a single apostrophe to the first element
                row[0] = "'" + row[0]
                print(f"{row[0]} is fixed")

            # Write the modified row to the output CSV
            writer.writerow(row)


def remove_apostrophy(file):
    filename = file[:-3]
    with open(file, "r", encoding="ISO-8859-1") as input_file, open(
        filename + "parsed.csv", "w", encoding="utf-8", newline=""
    ) as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        for row in reader:
            if row[0].startswith("'"):
                row[0] = row[0][1:]
                print(f"{row[0]} is fixed")

            writer.writerow(row)


if __name__ == "__main__":
    remove_apostrophy("/home/mr/Downloads/products-parsed.csv")
    # prepend_apostrophy_on_leading_zeros('./products.csv')
