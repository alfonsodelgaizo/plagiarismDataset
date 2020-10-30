#Prende in input il nome dell'algoritmo di clustering e la tipologia di embedding
# Come risultato genera nella cartella relativa all'algoritmo di cluster scelto (in Result_1_General)
# le volte in cui ogni coppia è stata inserita all'interno dello stesso cluster
# Infine dopo aver generato un file .csv del tipo coupleCnt_eng_50.csv stampa il grafico a barre

## -->>> python3 generateClusterCnt3.py NomeAlgoritmo TipoEmbedding <<<----

import xml.etree.ElementTree as ET
import csv
import sys
import os



class CntObject:
  def __init__(self, iteration,cnt,percentage):
    self.iteration = iteration
    self.cnt=cnt
    self.perc=percentage


def generateCSV():

    with open('./Results_3_General/'+algo+'/Panoramica/cnt_Div_'+embedding+'.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Clust_Div','Cnt','(%)'])
        i=0
        for l in range(0,len(arrayCnt)):
          filewriter.writerow([arrayCnt[i].iteration,arrayCnt[i].cnt,arrayCnt[i].perc])
          i=i+1




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



def read_CSV(filePath,nIteration):
    cntCouple=0
    filename='clusteCoupler'+nIteration+'.csv'
    path=filePath+filename
    with open(path) as csv_file:
     csv_reader = csv.reader(csv_file, delimiter=',')
     line_count = 0
     for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(row[1], row[2])
            cntCouple=cntCouple+1
            line_count += 1

    print(f'Processed {line_count} lines.')
    return cntCouple


arrayCnt=[]
algo='Kmean'
embedding= 'eng_300'

for i in range(2,25):
  filePath='./Results_3/'+algo+'/'+embedding+'/'
  nString=str(i)
  nCoppie=read_CSV(filePath,nString)
  perc=((52 - nCoppie) / 52) * 100
  percDef=100-perc
  percDef = round(percDef, 2)

  arrayCnt.append(CntObject(i,nCoppie,percDef))


for i in range(0,len(arrayCnt)):
    print(arrayCnt[i].iteration)
    print('PRESE:',arrayCnt[i].cnt)
    perc=round(arrayCnt[i].perc,2)
    print(perc)

generateCSV()
