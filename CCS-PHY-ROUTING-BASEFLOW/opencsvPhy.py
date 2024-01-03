import csv

filename = "custinfo.csv"

with open(filename, "r") as f:
    #x = f.read()
    #print(x)
    print(csv.DictReader(f))
    for line in csv.DictReader(f):
        line

