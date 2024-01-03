import csv

with open("custinfo.csv", "r") as data:
    reader = csv.reader(data)
    with open("custinfo.csv", "w") as out_data:
        writer = csv.writer(out_data)
        test_dict = {rows[0]:rows[1] for rows in reader}
        print(test_dict)

