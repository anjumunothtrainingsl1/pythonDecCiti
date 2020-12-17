import requests
import json
reqUrl="https://jsonplaceholder.typicode.com/posts"
response=requests.get(reqUrl)
print(response)
#print(response.content)
#print(response.json())

myDataInPython=json.dumps(response.json(),indent=4)
print(myDataInPython)
print("Status code",response.status_code)
print("Status message",response.reason)
print(response.text)
# response.headers- dict of header info
print("Header info",response.headers)
print("Header info",response.headers['Content-Type'])

#https://jsonplaceholder.typicode.com/posts?username=tom
requests.get(reqUrl,params={"username":"tom"})