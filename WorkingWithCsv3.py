import csv

with open(r"C:\Users\Administrator\Desktop\empFile.csv",mode="w") as writeFilePtr:
    writer=csv.writer(writeFilePtr,delimiter="$",quotechar='"',quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow([101,'Sara',789])
    writer.writerow([102, 'Lara', 1789])
    writer.writerow([103, 'Tara', 2789])