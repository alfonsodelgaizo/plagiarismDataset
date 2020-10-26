#Prende in input un numero intero che indica la coppia (0 a 51, descritte in tableCouple.csv) e permette di visualizzare
# nove grafici a barre relativi alle percentuali di clustering ottenute dalla coppia in analisi tra i vari
# algoritmi di clustering. I risultati che visualizza sono prelevati della cartella Percentage_1

# --->>> python3 multipleBar.py nCoppia <<<----

from plotly.subplots import make_subplots
import plotly.graph_objects as go
import os
import csv
import sys

class ArrayAlgoObject:
  def __init__(self, algoName, percArrayL, embeddingArrayL):
    self.algoName = algoName
    self.percArray = percArrayL
    self.embeddingArray = embeddingArrayL



resultArray = []

def read_CSV(filename, folderPath,algoName):
    path = folderPath + filename
    print("FILENAME" , path)

    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(row[4],'',row[5])
                s_embedding = row[4]
                s_perc= row[5]
                if (s_embedding=='50'):
                    embeddingArray.append('eng_50')
                if (s_embedding=='100'):
                    embeddingArray.append('eng_100')
                if (s_embedding=='150'):
                    embeddingArray.append('eng_150')
                if (s_embedding == '200'):
                    embeddingArray.append('eng_200')
                if (s_embedding == '300'):
                    embeddingArray.append('eng_300')

                perc=float(s_perc)
                percArray.append(perc)
                line_count += 1

    print(f'Processed {line_count} lines.')
    resultArray.append(ArrayAlgoObject(algoName, percArray, embeddingArray))


n_couple= sys.argv[1]
n_couple_str= str(n_couple)
algoArray=['KMean','BIRCH','MiniBatch100','MiniBatch250','MiniBatch500','MiniBatch1000','Spectral','GaussianMM','Agglomerative']
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

i=0
for j in range(0,len(algoArray)):
    embeddingArray = []
    percArray = []

    folderPath='./Percentage_2/'+algoArray[i]+'/'
    print(folderPath)
    for file in os.listdir(folderPath):
        try:
            if file.endswith((".csv")):
                print("CSV file found:\t", file)
                #Per ogni file nella cartella,leggilo
                n_couple=str(n_couple)
                fileNameInput=n_couple+'.csv'
                print('fileNameinput : ',fileNameInput)
                if (file==fileNameInput):
                        print('sono entrato')
                        read_CSV(file, folderPath,algoArray[i])
        except Exception as e:
            raise e
            print("No files found here!")

        title = song1CSV + ' - ' + song2CSV +' || '
        title=title.upper()
    i=i+1

# Initialize figure with subplots
fig = make_subplots(
    rows=3, cols=3, subplot_titles=(resultArray[0].algoName, resultArray[1].algoName,resultArray[2].algoName,resultArray[3].algoName,
                                    resultArray[4].algoName, resultArray[5].algoName,resultArray[6].algoName,resultArray[7].algoName,
                                    resultArray[8].algoName)
)

# Add traces

fig.add_trace(go.Bar(x=resultArray[0].embeddingArray, y=resultArray[0].percArray,), row=1, col=1)
fig.add_trace(go.Bar(x=resultArray[1].embeddingArray, y=resultArray[1].percArray,), row=1, col=2)
fig.add_trace(go.Bar(x=resultArray[2].embeddingArray, y=resultArray[2].percArray,), row=1, col=3)
fig.add_trace(go.Bar(x=resultArray[3].embeddingArray, y=resultArray[3].percArray,), row=2, col=1)
fig.add_trace(go.Bar(x=resultArray[4].embeddingArray, y=resultArray[4].percArray,), row=2, col=2)
fig.add_trace(go.Bar(x=resultArray[5].embeddingArray, y=resultArray[5].percArray,), row=2, col=3)
fig.add_trace(go.Bar(x=resultArray[6].embeddingArray, y=resultArray[6].percArray,), row=3, col=1)
fig.add_trace(go.Bar(x=resultArray[7].embeddingArray, y=resultArray[7].percArray,), row=3, col=2)
fig.add_trace(go.Bar(x=resultArray[8].embeddingArray, y=resultArray[8].percArray,), row=3, col=3)


# Update xaxis properties
fig.update_xaxes(title_text="Embedding", showgrid=False, row=1, col=1)
fig.update_xaxes(title_text="Embedding", showgrid=False, row=1, col=2)
fig.update_xaxes(title_text="Embedding", showgrid=False, row=1, col=3)
fig.update_xaxes(title_text="Embedding", showgrid=False, row=2, col=1)
fig.update_xaxes(title_text="Embedding", showgrid=False, row=2, col=2)
fig.update_xaxes(title_text="Embedding", showgrid=False, row=2, col=3)
fig.update_xaxes(title_text="Embedding", showgrid=False, row=3, col=1)
fig.update_xaxes(title_text="Embedding", showgrid=False, row=3, col=2)
fig.update_xaxes(title_text="Embedding", showgrid=False, row=3, col=3)


# Update yaxis properties
fig.update_yaxes(title_text="Percentage (%)", showgrid=False,range=[0,100],dtick=20, row=1, col=1)
fig.update_yaxes(title_text="Percentage (%)", showgrid=False,range=[0,100], dtick=20, row=1, col=2)
fig.update_yaxes(title_text="Percentage (%)", showgrid=False,range=[0,100],dtick=20,  row=1, col=3)
fig.update_yaxes(title_text="Percentage (%)", showgrid=False,range=[0,100],dtick=20,  row=2, col=1)
fig.update_yaxes(title_text="Percentage (%)", showgrid=False,range=[0,100],dtick=20,  row=2, col=2)
fig.update_yaxes(title_text="Percentage (%)", showgrid=False,range=[0,100],dtick=20,  row=2, col=3)
fig.update_yaxes(title_text="Percentage (%)", showgrid=False,range=[0,100],dtick=20,  row=3, col=1)
fig.update_yaxes(title_text="Percentage (%)", showgrid=False,range=[0,100],dtick=20,  row=3, col=2)
fig.update_yaxes(title_text="Percentage (%)", showgrid=False,range=[0,100], dtick=20, row=3, col=3)


#fig.update_layout(yaxis=dict(range=[0,100]),row=1, col=1)


# Update title and height
title = song1CSV + ' - ' + song2CSV

fig.update_layout(title_text=title)



fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7 ,row=1,col=1)
fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7, row=1,col=2)
fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7, row=1,col=3)
fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7, row=2,col=1)
fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7 ,row=2,col=2)
fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7, row=2,col=3)
fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7, row=3,col=1)
fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7, row=3,col=2)
fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7, row=3,col=3)


fig.show()