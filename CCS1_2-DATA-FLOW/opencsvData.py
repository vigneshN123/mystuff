import csv

filename = "data_flow.csv"

with open(filename, "r") as f:
    for line in csv.DictReader(f):
        line

