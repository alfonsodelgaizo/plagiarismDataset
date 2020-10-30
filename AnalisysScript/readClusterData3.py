import xml.etree.ElementTree as ET
import csv
import sys


class ClusterObject:
  def __init__(self, songName, cluster):
    self.songName = songName
    self.cluster = cluster

class CoupleClusterObject:
  def __init__(self, songName1,songName2, cluster1,cluster2):
    self.songName1 = songName1
    self.songName2 = songName2
    self.cluster_1 = cluster1
    self.cluster_2 = cluster2

print(sys.argv)
n_cluster= sys.argv[1]
t_embedding= sys.argv[2]
t_algo= sys.argv[3]

songArray = []
clusterArray = []
coupleArray = []

def generateCSV():

    cluster=str(n_cluster)
    with open('./Results_3/'+t_algo+'/'+t_embedding+'/clusteCoupler'+cluster+'.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['N','Song1','Song2', 'Cluster_1','Cluster_2'])
        i=0
        for l in range(0,len(coupleArray)):
            filewriter.writerow([i,coupleArray[i].songName1,coupleArray[i].songName2,coupleArray[i].cluster_1,coupleArray[i].cluster_2])
            i=i+1


def generateClusterArray():
    with open('cluster3.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(row[1], row[2])
                clusterArray.append(ClusterObject(row[1], row[2]))
                line_count += 1

        print(f'Processed {line_count} lines.')

    print('ARRAY GENERATO')

    for obj in clusterArray:
        print(obj.songName)
        print(obj.cluster)

def searchCluster(songName):

    print("SONGNAME1 :"+songName)

    for i in range(0,len(clusterArray)):
        if (clusterArray[i].songName == songName):
            return clusterArray[i].cluster


def generateSongArray():
    tree = ET.parse("dataset.xml")
    root = tree.getroot()


    for neighbor in root.iter('filename'):
        songArray.append(neighbor.text)


    print(songArray)


generateSongArray()
generateClusterArray()

i=0;
for j in range(0,len(songArray)):
  cluster_1=searchCluster(songArray[i])
  cluster_2=searchCluster(songArray[i+1])
  print(cluster_1)
  print(cluster_2)
  if (cluster_1== cluster_2):
      print("COPPIA :"+songArray[i]+"  "+songArray[i+1])
      coupleArray.append(CoupleClusterObject(songArray[i],songArray[i+1],cluster_1,cluster_2))

  i=i+2;

  if (i>=len(songArray)):
      break


generateCSV()
