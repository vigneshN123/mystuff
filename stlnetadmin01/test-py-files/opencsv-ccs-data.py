import csv

filename = "ccs-data.csv"

with open(filename, "r") as f:
    for line in csv.DictReader(f):
        line

