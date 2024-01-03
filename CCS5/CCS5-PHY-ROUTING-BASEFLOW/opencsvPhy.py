import csv

filename = "custinfo.csv"

with open(filename, "r") as f:
    for line in csv.DictReader(f):
        line

