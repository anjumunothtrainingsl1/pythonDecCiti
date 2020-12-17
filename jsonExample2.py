import json

with open("zipcode.json",mode="r") as readFilePtr:
    deserialisedData=json.load(readFilePtr)
    #print(deserialisedData["zipcodeDetails"][0])
    for i in range(len(deserialisedData["zipcodeDetails"])):
        print(deserialisedData["zipcodeDetails"][i])

