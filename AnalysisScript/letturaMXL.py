import xml.etree.ElementTree as ET

tree = ET.parse("dataset.xml")
root = tree.getroot()
songArray = []



for neighbor in root.iter('filename'):
    songArray.append(neighbor.text)


print(songArray)

i=0;
for j in range(0,len(songArray)):

  print("COPPIA :"+songArray[i]+"  "+songArray[i+1])

  i=i+2;