#Prende in input il nome dell'algoritmo di cluster e stampa una panoramica degli accoppiamenti per la prima e la seconda metrica
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


resultArray1 = []
resultArray2 = []

def read_CSV(filepath,fileName,metric):

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

    if(metric==1):
      resultArray1.append(ArrayAlgoObject(fileName,indArray,clusterArray,namesCouple,coupleColor))
    if(metric==2):
      resultArray2.append(ArrayAlgoObject(fileName,indArray,clusterArray,namesCouple,coupleColor))
    print(f'Processed {line_count} lines.')


algo=sys.argv[1]
folderPath1='./Results_1_General/'+algo+'/'
folderPath2='./Results_2_General/'+algo+'/'

print(folderPath1)
for file in os.listdir(folderPath1):

    try:
            indArray = []
            clusterArray = []
            namesCouple = []
            coupleColor = []
            if file.endswith((".csv")):
                print("CSV file found:\t", file)
                #Per ogni file nella cartella,leggilo
                filePath=folderPath1+file
                read_CSV(filePath,file,1)

    except Exception as e:
            raise e
            print("No files found here!")

print(folderPath2)
for file in os.listdir(folderPath2):

    try:
            indArray = []
            clusterArray = []
            namesCouple = []
            coupleColor = []
            if file.endswith((".csv")):
                print("CSV file found:\t", file)
                #Per ogni file nella cartella,leggilo
                filePath=folderPath2+file
                read_CSV(filePath,file,2)

    except Exception as e:
            raise e
            print("No files found here!")

# Initialize figure with subplots
fig = make_subplots(
    rows=5, cols=2, subplot_titles=(resultArray1[0].title,resultArray2[0].title,resultArray1[1].title,resultArray2[1].title,
                                    resultArray1[2].title,resultArray2[2].title,resultArray1[3].title,resultArray2[3].title,
                                    resultArray1[4].title,resultArray2[4].title,)
)

# Add traces

fig.add_trace(go.Bar(x=resultArray1[0].indArray, y=resultArray1[0].clusterArray), row=1, col=1)
fig.add_trace(go.Bar(x=resultArray2[0].indArray, y=resultArray2[0].clusterArray), row=1, col=2)
fig.add_trace(go.Bar(x=resultArray1[1].indArray, y=resultArray1[1].clusterArray), row=2, col=1)
fig.add_trace(go.Bar(x=resultArray2[1].indArray, y=resultArray2[1].clusterArray), row=2, col=2)
fig.add_trace(go.Bar(x=resultArray1[2].indArray, y=resultArray1[2].clusterArray), row=3, col=1)
fig.add_trace(go.Bar(x=resultArray2[2].indArray, y=resultArray2[2].clusterArray), row=3, col=2)
fig.add_trace(go.Bar(x=resultArray1[3].indArray, y=resultArray1[3].clusterArray), row=4, col=1)
fig.add_trace(go.Bar(x=resultArray2[3].indArray, y=resultArray2[3].clusterArray), row=4, col=2)
fig.add_trace(go.Bar(x=resultArray1[4].indArray, y=resultArray1[4].clusterArray), row=5, col=1)
fig.add_trace(go.Bar(x=resultArray2[4].indArray, y=resultArray2[4].clusterArray), row=5, col=2)





# Update yaxis properties
fig.update_yaxes(title_text="Cluster", showgrid=False,range=[0,69],dtick=10, row=1, col=1)
fig.update_yaxes(title_text="Cluster", showgrid=False,range=[0,69], dtick=10, row=1, col=2)
fig.update_yaxes(title_text="Cluster", showgrid=False,range=[0,69],dtick=10,  row=2, col=1)
fig.update_yaxes(title_text="Cluster", showgrid=False,range=[0,69],dtick=10,  row=2, col=2)
fig.update_yaxes(title_text="Cluster", showgrid=False,range=[0,69],dtick=10,  row=3, col=1)
fig.update_yaxes(title_text="Cluster", showgrid=False,range=[0,69],dtick=10,  row=3, col=2)
fig.update_yaxes(title_text="Cluster", showgrid=False,range=[0,69], dtick=10, row=4, col=1)
fig.update_yaxes(title_text="Cluster", showgrid=False,range=[0,69],dtick=10,  row=4, col=2)
fig.update_yaxes(title_text="Cluster", showgrid=False,range=[0,69],dtick=10,  row=5, col=1)
fig.update_yaxes(title_text="Cluster", showgrid=False,range=[0,69],dtick=10,  row=5, col=2)


#fig.update_layout(yaxis=dict(range=[0,100]),row=1, col=1)


# Update title and height

title = algo

fig.update_layout(title_text=title)



fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7 ,row=1,col=1)
fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7, row=1,col=2)
fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7, row=2,col=1)
fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7, row=2,col=2)
fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7 ,row=3,col=1)
fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7 ,row=3,col=2)
fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7, row=4,col=1)
fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7, row=4,col=2)
fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7, row=5,col=1)
fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7 ,row=5,col=2)


fig.show()