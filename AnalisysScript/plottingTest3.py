import plotly.express as px
import csv
import sys
import pandas as pd

algo_name=sys.argv[1]
embedding=sys.argv[2]

title= algo_name+'_'+embedding

clusterArray=[]
namesCouple = []
indArray = []
coupleColor =[]


path='./Results_3_General/'+algo_name+'/coupleCnt_'+embedding+'.csv'
print(path)
with open(path) as csv_file:
 csv_reader = csv.reader(csv_file, delimiter=',')
 line_count = 0
 for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #print(row[0], row[3])
            indArray.append(row[0])
            clusterArray.append(row[3])
            singleNameCouple= row[1]+' - '+row [2]
            namesCouple.append(singleNameCouple)
            n_cluster= int(row[3])
            if (n_cluster>=0 and  n_cluster<=6):
                coupleColor.append("VeryLow")
            if ( n_cluster>=7 and n_cluster<=11):
                coupleColor.append("Low")
            if ( n_cluster >= 12 and  n_cluster <= 16):
                coupleColor.append("Medium")
            if ( n_cluster >= 17 and  n_cluster <= 20):
                coupleColor.append("High")
            if (n_cluster >= 21 and n_cluster <= 25):
                coupleColor.append("VeryHigh")
#df = pd.DataFrame(clusterArray, columns=['n_cluster'], index=indArray)
# Sample data

print(len(clusterArray))
print(len(namesCouple))
print(len(indArray))
print(len(coupleColor))

d={
   'NameCouple': namesCouple,
   'Coppia': indArray,
   'Cluster':clusterArray,
   'CoupleMatching': coupleColor
  }

df=pd.DataFrame(d)
print(df)
#fig = px.bar(df, y="n_cluster", title='Kmean_eng_200')

# plot structure
fig = px.bar(df,
             x='Coppia',
             y='Cluster',
             title=title,
             color="CoupleMatching",
             color_discrete_map={
                "VeryLow": "#F5F5F5",
                "Low": "#bada55",
                "Medium": "#FFD700",
                "High": "#FA8072",
                "VeryHigh": "#8B0000"},
                         )



fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))

fig.update_xaxes(dtick=2)
fig.update_yaxes(dtick=3)


fig.update_traces( marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.7)

fig.show()