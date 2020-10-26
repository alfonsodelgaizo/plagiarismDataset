#Prende in input il nome dell'algoritmo di cluster ed il tipo di metrica(1 o 2), successivamente stampa i 5 grafici relativi al clustering
# differenziato da i vari embedding(50,100,150,200,300)

# --->>> python3 multipleBarCnt.py Algo 1 <<<----

from plotly.subplots import make_subplots
import plotly.graph_objects as go
import os
import csv
import sys

class ArrayAlgoObject:
  def __init__(self, title,indArray, clusterArray, namesCouple,coupleColor):
    self.title=title
    self.indArray= indArray
    self.clusterArray = clusterArray
    self.namesCouple = namesCouple
    self.coupleColor= coupleColor


resultArray = []

def read_CSV(filepath,fileName):

    print("FILEPATH" , filepath)

    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # print(row[0], row[3])
                indArray.append(row[0])
                clusterArray.append(row[3])
                singleNameCouple = row[1] + ' - ' + row[2]
                namesCouple.append(singleNameCouple)
                n_cluster = int(row[3])
                if (n_cluster >= 0 and n_cluster <= 15):
                    coupleColor.append("VeryLow")
                if (n_cluster >= 16 and n_cluster <= 25):
                    coupleColor.append("Low")
                if (n_cluster >= 26 and n_cluster <= 35):
                    coupleColor.append("Medium")
                if (n_cluster >= 36 and n_cluster <= 50):
                    coupleColor.append("High")
                if (n_cluster >= 51 and n_cluster <= 70):
                    coupleColor.append("VeryHigh")

    resultArray.append(ArrayAlgoObject(fileName,indArray,clusterArray,namesCouple,coupleColor))
    print(f'Processed {line_count} lines.')


algo=sys.argv[1]
result=sys.argv[2]
if (result=='1'):
    folderPath='./Results_1_General/'+algo+'/'
if (result=='2'):
    folderPath='./Results_2_General/'+algo+'/'

print(folderPath)
for file in os.listdir(folderPath):

    try:
            indArray = []
            clusterArray = []
            namesCouple = []
            coupleColor = []
            if file.endswith((".csv")):
                print("CSV file found:\t", file)
                #Per ogni file nella cartella,leggilo
                filePath=folderPath+file
                read_CSV(filePath,file)

    except Exception as e:
            raise e
            print("No files found here!")

# Initialize figure with subplots
fig = make_subplots(
    rows=2, cols=3, subplot_titles=(resultArray[0].title, resultArray[1].title,resultArray[2].title,resultArray[3].title,resultArray[4].title)
)

# Add traces

fig.add_trace(go.Bar(x=resultArray[0].indArray, y=resultArray[0].clusterArray), row=1, col=1)
fig.add_trace(go.Bar(x=resultArray[1].indArray, y=resultArray[1].clusterArray), row=1, col=2)
fig.add_trace(go.Bar(x=resultArray[2].indArray, y=resultArray[2].clusterArray), row=1, col=3)
fig.add_trace(go.Bar(x=resultArray[3].indArray, y=resultArray[3].clusterArray), row=2, col=1)
fig.add_trace(go.Bar(x=resultArray[4].indArray, y=resultArray[4].clusterArray), row=2, col=2)



# Update xaxis properties
fig.update_xaxes(title_text="Coppia", showgrid=False, dtick=2,row=1, col=1)
fig.update_xaxes(title_text="Coppia", showgrid=False,dtick=2, row=1, col=2)
fig.update_xaxes(title_text="Coppia", showgrid=False,dtick=2, row=1, col=3)
fig.update_xaxes(title_text="Coppia", showgrid=False,dtick=2, row=2, col=1)
fig.update_xaxes(title_text="Coppia", showgrid=False,dtick=2, row=2, col=2)


# Update yaxis properties
fig.update_yaxes(title_text="Cluster", showgrid=False,range=[0,69],dtick=10, row=1, col=1)
fig.update_yaxes(title_text="Cluster", showgrid=False,range=[0,69], dtick=10, row=1, col=2)
fig.update_yaxes(title_text="Cluster", showgrid=False,range=[0,69],dtick=10,  row=1, col=3)
fig.update_yaxes(title_text="Cluster", showgrid=False,range=[0,69],dtick=10,  row=2, col=1)
fig.update_yaxes(title_text="Cluster", showgrid=False,range=[0,69],dtick=10,  row=2, col=2)



#fig.update_layout(yaxis=dict(range=[0,100]),row=1, col=1)


# Update title and height
if (result=='1'):
   title=algo+' - 1° Metric'
if (result=='2'):
    title = algo + ' - 2° Metric'

fig.update_layout(title_text=title)



fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7 ,row=1,col=1)
fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7, row=1,col=2)
fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7, row=1,col=3)
fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7, row=2,col=1)
fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7 ,row=2,col=2)



fig.show()