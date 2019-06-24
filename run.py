import json
import xlsxwriter

with open('options.json') as f:
    data = json.load(f)

print(data['name'] +"  "+ data['languages'][0])


# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
#{
#    "name": "Bob",
#    "languages": [
#        "English",
#        "Fench"
#    ]
#}