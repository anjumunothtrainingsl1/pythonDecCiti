import csv

data=[{
  "_id": "01350",
  "city": "MONROE",
  "loc": [
    -72.960156,
    42.723885
  ],
  "pop": 97,
  "state": "MA"
},{
  "_id": "02713",
  "city": "CUTTYHUNK",
  "loc": [
    -70.87854,
    41.443601
  ],
  "pop": 98,
  "state": "MA"
},{
  "_id": "04442",
  "city": "GREENVILLE JUNCT",
  "loc": [
    -69.637526,
    45.488394
  ],
  "pop": 99,
  "state": "ME"
},{
  "_id": "05748",
  "city": "HANCOCK",
  "loc": [
    -72.913285,
    43.912525
  ],
  "pop": 98,
  "state": "VT"
},{
  "_id": "11967",
  "city": "SHIRLEY",
  "loc": [
    -72.876043,
    40.743932
  ],
  "pop": 97,
  "state": "NY"
},{
  "_id": "16565",
  "city": "ERIE",
  "loc": [
    -80.10011,
    42.0687
  ],
  "pop": 97,
  "state": "PA"
},{
  "_id": "17888",
  "city": "WILBURTON",
  "loc": [
    -76.392922,
    40.812087
  ],
  "pop": 98,
  "state": "PA"
},{
  "_id": "23418",
  "city": "ONLEY",
  "loc": [
    -75.6992,
    37.670422
  ],
  "pop": 97,
  "state": "VA"
},{
  "_id": "25115",
  "city": "KANAWHA FALLS",
  "loc": [
    -81.162753,
    38.107932
  ],
  "pop": 98,
  "state": "WV"
},{
  "_id": "25847",
  "city": "SULLIVAN",
  "loc": [
    -81.13048,
    37.790384
  ],
  "pop": 99,
  "state": "WV"
},{
  "_id": "26680",
  "city": "RUSSELVILLE",
  "loc": [
    -80.885777,
    38.10829
  ],
  "pop": 99,
  "state": "WV"
},{
  "_id": "30148",
  "city": "MARBLE HILL",
  "loc": [
    -84.337151,
    34.415353
  ],
  "pop": 98,
  "state": "GA"
},{
  "_id": "37332",
  "city": "EVENSVILLE",
  "loc": [
    -85.022773,
    35.615346
  ],
  "pop": 99,
  "state": "TN"
},{
  "_id": "40807",
  "city": "BENHAM",
  "loc": [
    -82.909399,
    36.957377
  ],
  "pop": 98,
  "state": "KY"
},{
  "_id": "55111",
  "city": "FORT SNELLING",
  "loc": [
    -93.202579,
    44.901548
  ],
  "pop": 97,
  "state": "MN"
},{
  "_id": "59420",
  "city": "CARTER",
  "loc": [
    -110.978593,
    47.780964
  ],
  "pop": 99,
  "state": "MT"
},{
  "_id": "59642",
  "city": "RINGLING",
  "loc": [
    -110.824214,
    46.285468
  ],
  "pop": 97,
  "state": "MT"
},{
  "_id": "59916",
  "city": "ESSEX",
  "loc": [
    -113.946678,
    48.494028
  ],
  "pop": 98,
  "state": "MT"
},{
  "_id": "59928",
  "city": "POLEBRIDGE",
  "loc": [
    -114.383558,
    48.820585
  ],
  "pop": 97,
  "state": "MT"
},{
  "_id": "65758",
  "city": "SYCAMORE",
  "loc": [
    -92.354355,
    36.67179
  ],
  "pop": 97,
  "state": "MO"
},{
  "_id": "67071",
  "city": "LAKE CITY",
  "loc": [
    -98.809833,
    37.356885
  ],
  "pop": 97,
  "state": "KS"
},{
  "_id": "67472",
  "city": "OAKHILL",
  "loc": [
    -97.330501,
    39.247668
  ],
  "pop": 96,
  "state": "KS"
},{
  "_id": "74754",
  "city": "RINGOLD",
  "loc": [
    -95.070387,
    34.179892
  ],
  "pop": 97,
  "state": "OK"
},{
  "_id": "82052",
  "city": "BUFORD",
  "loc": [
    -105.469697,
    41.142115
  ],
  "pop": 97,
  "state": "WY"
},{
  "_id": "82332",
  "city": "SAVERY",
  "loc": [
    -107.42338,
    41.039485
  ],
  "pop": 97,
  "state": "WY"
},{
  "_id": "82428",
  "city": "HYATTVILLE",
  "loc": [
    -107.605318,
    44.250693
  ],
  "pop": 97,
  "state": "WY"
},{
  "_id": "87573",
  "city": "TERERRO",
  "loc": [
    -105.645725,
    35.736881
  ],
  "pop": 99,
  "state": "NM"
},{
  "_id": "87943",
  "city": "WINSTON",
  "loc": [
    -107.667456,
    33.306089
  ],
  "pop": 97,
  "state": "NM"
},{
  "_id": "89017",
  "city": "HIKO",
  "loc": [
    -115.177158,
    37.651695
  ],
  "pop": 97,
  "state": "NV"
},{
  "_id": "95728",
  "city": "SODA SPRINGS",
  "loc": [
    -120.465493,
    39.338467
  ],
  "pop": 96,
  "state": "CA"
},{
  "_id": "97751",
  "city": "PAULINA",
  "loc": [
    -119.782768,
    44.210243
  ],
  "pop": 98,
  "state": "OR"
},{
  "_id": "98158",
  "city": "SEATAC",
  "loc": [
    -122.318454,
    47.442739
  ],
  "pop": 97,
  "state": "WA"
},{
  "_id": "99574",
  "city": "CHENEGA BAY",
  "loc": [
    -147.943316,
    60.102558
  ],
  "pop": 96,
  "state": "AK"
},{
  "_id": "99788",
  "city": "CHALKYITSIK",
  "loc": [
    -143.638121,
    66.719
  ],
  "pop": 99,
  "state": "AK"
}]

with open(r"C:\Users\Administrator\Desktop\zip1.csv",mode="w") as writeFilePtr:
    fName=["_id","city","loc","pop","state"]
    writer=csv.DictWriter(writeFilePtr,fieldnames=fName)
    writer.writeheader()
    for i in range(len(data)):
        writer.writerow(data[i])

