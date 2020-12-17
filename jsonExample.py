# Serialising Json
#Python
import json
data={"empDict":{"empId":101,"empName":"sara","hobbies":["singing","dancing"],"salary":78.67,"projects":("P1","P2","P3"),"submittedAadhaar":True}}

with open("empjson.json",mode="w") as writeFilePtr:
    json.dump(data,writeFilePtr)

dataInJsonFormat=json.dumps(data,indent=4)
print(dataInJsonFormat)