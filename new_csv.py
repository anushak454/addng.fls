import csv

with open("test.csv", "r") as file:
    file = csv.reader(file)
    print(file)


