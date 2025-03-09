# GET

# use requests library

import requests

api_url="https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print(response.status_code)
print(response.headers["content-type"])
print(response.json())

# POST
api_url="https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False} # create a dictionary ti simulate a json object
                                   # request.post() serializes the dictionary to json
response = requests.post(api_url, json=todo)
print(response.json())
# If you don’t use the json keyword argument to supply the JSON data, then you need to set Content-Type accordingly and serialize the JSON manually.
import json
headers = {"Content-Type": "application/json"}
todo2 = {"userId": 1, "title": "Buy apples", "completed": False}
response2 = requests.post(api_url, data=json.dumps(todo2), headers=headers)
print(response2.json())


# PUT
api_url="https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())

todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo)
print(response.json())
