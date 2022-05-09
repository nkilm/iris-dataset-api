import numpy as np
import requests
import json

headers = {}
headers["Content-Type"] = "application/json"
payload = {'data': json.dumps([4.5,2.5,3.5,2])}

res = requests.post('http://127.0.0.1:5050/iris', json=payload,headers=headers).json()

# Make array from the list
res = np.array(res)
print(res)