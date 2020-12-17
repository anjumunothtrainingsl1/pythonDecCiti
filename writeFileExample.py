try:
    with open("sample2.txt",mode="r",encoding="utf-8") as readFilePtr:
        print(readFilePtr.read(4))
        print(readFilePtr.read(10))
        print("Current position in the file",readFilePtr.tell())
        readFilePtr.seek(12)
        print(readFilePtr.read(4))
        readFilePtr.seek(0)
        for line in readFilePtr:
            print(line,end=" ")
        print("*"*30)
        # readLine
        readFilePtr.seek(0)
        print(readFilePtr.readline())
except NameError:
    print("Error in file operation")

except FileNotFoundError:
    print("File does not exists")
