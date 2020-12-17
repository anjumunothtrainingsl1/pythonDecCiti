import csv


with open(r"C:\Users\Administrator\Desktop\zipcode1.csv",mode="r") as readfilePtr:
    csvReader=csv.reader(readfilePtr,delimiter=",")
    headerLine=0
    for row in csvReader:
        if headerLine ==0:
            for item in row:
                print(item, end ="    ")
            print()
            headerLine+=1
        else:
            for item in row:
                print(item, end="    ")
            print()
            

