import xml.etree.ElementTree as ET
import csv

class CoupleClusterObject:
  def __init__(self, songName1,songName2):
    self.songName1 = songName1
    self.songName2 = songName2

songArray = []
coupleArray=[]

tree = ET.parse("dataset.xml")
root = tree.getroot()

for neighbor in root.iter('filename'):
    songArray.append(neighbor.text)

print(songArray)

i = 0
for j in range(0, len(songArray)):
    coupleArray.append(CoupleClusterObject(songArray[i], songArray[i + 1]))
    i = i + 2;
    if (i >= len(songArray)):
        break


with open('tableCouple.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['N','Song1','Song2'])
        i=0
        for l in range(0,len(coupleArray)):
            filewriter.writerow([i,coupleArray[i].songName1,coupleArray[i].songName2])
            i=i+1


