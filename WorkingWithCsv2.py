import csv

with open(r"C:\Users\Administrator\Desktop\zipcode1.csv", mode="r") as readfilePtr:
    dictData = csv.DictReader(readfilePtr)
    for row in dictData:
        print(row["city"], ":", row["pop"])

