with open(r"C:\Users\Administrator\Desktop\text1.properties",mode="r") as readFilePtr:
    listOfValues=[]
    for row in readFilePtr:
        myStr=row
        list1=myStr.split("=")
        myDict={}
        myDict[list1[0]]=list1[1]
        listOfValues.append(myDict)
    print(listOfValues)

    

