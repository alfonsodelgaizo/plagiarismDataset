import csv
import re

#Classe utile per associare al nome della canzone letta l'array numerico corrispondente

class ArraySongObject:
  def __init__(self, songName, songArray):
    self.songName = songName
    self.songArray = songArray

arraySongObjectList=[]

def generaArray(songName,songString):
    numericalArray=[]

    #print(re.findall(r'[+-]?\d+(?:\.\d+)?', songString))
    #carico l'array generato dalla funzione findall in numericalArray
    newsongString = songString.replace("p", "0")


    numericalArray=re.findall(r'[+-]?\d+(?:\.\d+)?', newsongString);


    arraySongObjectList.append(ArraySongObject(songName,numericalArray))


with open('datasetParsingDEF.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(row[1],row[2])
            generaArray(row[1],row[2])
            line_count += 1

    print(f'Processed {line_count} lines.')

print('ARRAY GENERATO')

for obj in arraySongObjectList:
    print(obj.songName)
    print(obj.songArray)
