from openpyxl.styles import NamedStyle, Font, Border, Side
import json
import xlsxwriter
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
from pathlib import Path

with open('options.json') as f:
    data = json.load(f)

print(data['name'] + "  " + data['languages'][0])
wb = load_workbook(filename = Path('in\\a.xlsx'))
#wb = Workbook('in\a.xlsx')
sheet_ranges = wb['Sheet1']
print(sheet_ranges['D18'].value)
ws = wb.active

highlight1 = NamedStyle(name="highlight")
highlight1.font = Font(bold=True, size=20)
bd = Side(style='thick', color="000000")
highlight1.border = Border(left=bd, top=bd, right=bd, bottom=bd)
wb.add_named_style(highlight1)

ws['E9'].style = highlight1

wb.close()
print("done")

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
# {
#    "name": "Bob",
#    "languages": [
#        "English",
#        "Fench"
#    ]
# }
