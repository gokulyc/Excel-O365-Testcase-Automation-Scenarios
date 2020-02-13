import xml.etree.ElementTree as ET
tree = ET.parse(r'PyL1Assignment\8xml\input.xml')
root = tree.getroot()
print(root,'\ntags :',root.tag,'\nattributes:',root.attrib)

for elem in root:
   for subelem in elem:
      print(subelem.text)