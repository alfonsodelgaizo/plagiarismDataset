#Prende in input il numero di coppia (presente in tableCouple.csv) e il nome dell'algoritmo.
#Legge il file da Percentage_1/NomeAlgoritmo e stampa i risulti ottenuti da main_PercCSV.py

# --->>> python3 plottingCouple_Perc2.py numeroCoppia Algoritmo <<<----

import os
import plotly.express as px
import sys
import csv

embeddingArray= []
percArray= []

def read_CSV(filename, folderPath):
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

n_couple= sys.argv[1]
n_couple_str= str(n_couple)
algo=sys.argv[2]
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


folderPath='./Percentage_2/'+algo+'/'

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
                    read_CSV(file, folderPath)
    except Exception as e:
        raise e
        print("No files found here!")

title = song1CSV + ' - ' + song2CSV +' || '+ algo
title=title.upper()
fig = px.histogram(x=embeddingArray, y=percArray,
                   color =embeddingArray,
                   title=title
                   )

fig.update_xaxes(title_text='Embedding')
fig.update_yaxes(title_text='Percentage (%)')

fig.update_layout(yaxis=dict(range=[0,100]))


fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))

fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7)


fig.show()