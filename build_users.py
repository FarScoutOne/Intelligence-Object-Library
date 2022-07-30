import json
from user import User

# The JSON object deserializes into a Python dictionary and is saved
# into the variable 'users'.
user_dict = {}

with open("user_data.json") as complex_data:
    data = complex_data.read()
    users = json.loads(data)

for user in users:
    user_string = users[user]
    user_string = json.dumps(user_string)
    user_decoded = json.loads(user_string, object_hook=User.from_json)
    user_dict[user_decoded.fname.lower() + '_' + user_decoded.lname.lower()] = (user_decoded)
