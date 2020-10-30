#Prende in input il nome dell'algoritmo di clustering e la tipologia di embedding
# Come risultato genera nella cartella relativa all'algoritmo di cluster scelto (in Result_1_General)
# le volte in cui ogni coppia è stata inserita all'interno dello stesso cluster
# Infine dopo aver generato un file .csv del tipo coupleCnt_eng_50.csv stampa il grafico a barre

## -->>> python3 generateClusterCnt3.py NomeAlgoritmo TipoEmbedding <<<----

import xml.etree.ElementTree as ET
import csv
import sys
import os

class CoupleClusterObject:
  def __init__(self, songName1,songName2):
    self.songName1 = songName1
    self.songName2 = songName2

class CoupleCntObject:
  def __init__(self, songName1,songName2,cnt):
    self.songName1 = songName1
    self.songName2 = songName2
    self.cnt=cnt


def generateCSV():

    with open('./Results_3_General/'+algo+'/coupleCnt_'+embedding+'.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['N','Song1','Song2','Cnt'])
        i=0
        for l in range(0,len(coupleArray)):
            filewriter.writerow([i,coupleCntArray[i].songName1,coupleCntArray[i].songName2,coupleCntArray[i].cnt])
            i=i+1

def generateSongArray():
    tree = ET.parse("dataset.xml")
    root = tree.getroot()


    for neighbor in root.iter('filename'):
        songArray.append(neighbor.text)

    #print(songArray)

def generateCoupleArray():
    i=0
    for j in range(0, len(songArray)):
        coupleArray.append(CoupleClusterObject(songArray[i], songArray[i + 1]))
        i = i + 2;
        if (i >= len(songArray)):
            break


def folderRead(folderPath,song1,song2):
    location = os.getcwd()  # get present working directory location here
    counter = 0  # keep a count of all files found
    csvfiles = []  # list to store all csv files found at location
    cntDef=0;

    for file in os.listdir(folderPath):
        try:
            if file.endswith((".csv")):
                print("CSV file found:\t", file)
                cntCoupleSingle=read_CSV(file,folderPath,song1,song2)
                cntDef= cntDef + cntCoupleSingle
                counter = counter + 1
        except Exception as e:
            raise e
            print("No files found here!")

    print("Total files found:\t", counter)

    #generateCSV();
    print("-------- END ----------")
    coupleCntArray.append(CoupleCntObject(song1,song2,cntDef))



def read_CSV(filename,folderPath,song1,song2):
    cntCouple=0
    print("FILENAME"+filename)
    path=folderPath+filename
    with open(path) as csv_file:
     csv_reader = csv.reader(csv_file, delimiter=',')
     line_count = 0
     for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(row[1], row[2])
            song1CSV=row[1]
            song2CSV=row[2]
            if (song1CSV==song1 and song2CSV==song2):
             print("entra")
             cntCouple=cntCouple+1
            line_count += 1

    print(f'Processed {line_count} lines.')
    return cntCouple


songArray = []
coupleArray = []
coupleCntArray = []

generateSongArray()
generateCoupleArray()

algo=sys.argv[1]
embedding=sys.argv[2]

i=0;
for j in range(0,len(coupleArray)):
   song1=coupleArray[i].songName1
   song2=coupleArray[i].songName2
   folderRead('./Results_3/'+algo+'/'+embedding+'/',song1,song2)
   i=i+1


for j in range(0,len(coupleCntArray)):
    print(coupleCntArray[j].songName1, "  - ",coupleCntArray[j].songName2 , " - ",coupleCntArray[j].cnt)

generateCSV()

sys.argv = ['./plottingTest3.py',algo,embedding]
exec(open("./plottingTest3.py").read())