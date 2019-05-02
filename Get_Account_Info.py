import json
with open('../../Account.json', 'r') as json_data:
    data = json.loads(json_data.read())
    print(data)
    print(data['NFU']['Account_name'])
    print(data['NFU']['Password'])
