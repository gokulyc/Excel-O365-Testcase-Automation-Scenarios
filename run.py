import json
with open('options.json') as f:
    data = json.load(f)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
#{
#    "name": "Bob",
#    "languages": [
#        "English",
#        "Fench"
#    ]
#}
print(data['name'] + data['languages'])


