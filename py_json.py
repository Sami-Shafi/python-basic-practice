# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

# sample JSON
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 16, "email": "john@example.com"}'

# parse
user = json.loads(userJSON)
print(user["first_name"])

# stringify
phones = {"brand": "Realme", "Model": "C11", "Owner": "Sami"}
phoneJSON = json.dumps(phones)
print(type(phoneJSON))