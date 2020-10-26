import sys
import csv
import os

class CoupleClusterObject:
  def __init__(self, songName1,songName2,algo,embedding,perc):
    self.songName1 = songName1
    self.songName2 = songName2
    self.algo= algo
    self.embedding=embedding
    self.perc= perc


def generateCSV():

    with open('./Percentage_2/'+algo+'/'+n_couple_str+'.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['N','Song1','Song2','Algo','Embedding','Perc'])
        i=0
        for l in range(0,len(arrayPerc)):
            filewriter.writerow([i,arrayPerc[i].songName1,arrayPerc[i].songName2
                                    ,arrayPerc[i].algo,arrayPerc[i].embedding,arrayPerc[i].perc])
            i=i+1

def read_CSV(filename, folderPath, song1, song2):
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
            song1CSVf=row[1]
            song2CSVf=row[2]
            if (song1CSVf==song1 and song2CSVf==song2):
                 print("entra")
                 cnt=int(row[3])
                 print("CNT:",cnt)
                 perc=((69-cnt)/69)*100
                 percDef=100-perc
                 return percDef

            line_count += 1

    print(f'Processed {line_count} lines.')


n_couple= sys.argv[2]
n_couple_str= str(n_couple)
algo=sys.argv[1]
n_couple= int(n_couple)
arrayPerc=[]

path = "./tableCouple.csv"
with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #print(row[1], row[2])
            if (line_count==n_couple+1):
                print("entra")
                song1CSV = row[1]
                song2CSV = row[2]

            line_count += 1

print(f'Processed {line_count} lines.')

print(song1CSV)
print(song2CSV)

folderPath='./Results_2_General/'+algo+'/'
for file in os.listdir(folderPath):
    try:
        if file.endswith((".csv")):
            print("CSV file found:\t", file)
            #Per ogni file nella cartella,leggilo
            percDef = read_CSV(file, folderPath, song1CSV, song2CSV)
            print("PERCDEF: ",percDef)
            percDef = "{:.2f}".format(percDef)
            percDef=float(percDef)
            if (file == 'coupleCnt_eng_50.csv'):
                embedding = 50
            if (file== 'coupleCnt_eng_100.csv'):
                embedding = 100
            if (file== 'coupleCnt_eng_150.csv'):
                embedding = 150
            if (file == 'coupleCnt_eng_200.csv'):
                embedding = 200
            if (file == 'coupleCnt_eng_300.csv'):
                embedding = 300
            arrayPerc.append(CoupleClusterObject(song1CSV,song2CSV,algo,embedding,percDef))

    except Exception as e:
        raise e
        print("No files found here!")


for i in range(0,len(arrayPerc)):
   print(arrayPerc[i].perc)

generateCSV()