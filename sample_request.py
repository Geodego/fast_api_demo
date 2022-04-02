"""
Script used for running the post.
"""
import requests
import json

# We define the data we want to pass in
data = {"name": "Kit", "tags": ["book", "towel"], "item_id": 23}

r = requests.post("http://127.0.0.1:8000/items/", data=json.dumps(data))

print(r.json)