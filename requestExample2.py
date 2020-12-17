import requests
reqUrl="https://jsonplaceholder.typicode.com/posts"

response=requests.post(reqUrl,data={"postId":101})
print(response.json())
print(response.status_code)