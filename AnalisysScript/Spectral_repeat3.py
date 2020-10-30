import chars2vec
import csv
import random
import sys
from sklearn.cluster import SpectralClustering


# Load Inutition Engineering pretrained model
# Models names: 'eng_50', 'eng_100', 'eng_150' 'eng_200', 'eng_300'

print(sys.argv)
print(sys.argv[1])
n_cluster= sys.argv[1]
#n_cluster= int(n_cluster_Param)
t_embedding=sys.argv[2]

# Models names: 'eng_50', 'eng_100', 'eng_150' 'eng_200', 'eng_300'

if (t_embedding=='50'):
    embedding='eng_50'
if (t_embedding=='100'):
    embedding='eng_100'
if (t_embedding=='150'):
    embedding='eng_150'
if (t_embedding=='200'):
    embedding='eng_200'
if (t_embedding=='300'):
    embedding='eng_300'



label_color = []

for i in range(0,n_cluster+1):
    r = lambda: random.randint(0, 255)
    esadecimale='#%02X%02X%02X' % (r(), r(), r())
    label_color.append(esadecimale)

def generateCSV(labels,name):

    with open('cluster3.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['N','Song', 'Cluster'])
        i=0
        for l in labels:
            single_Name = name[i][:-4]
            filewriter.writerow([i,single_Name,l])
            i=i+1


c2v_model = chars2vec.load_model(embedding)

words=[]
etichette=[]

with open('datasetParsing3DEF.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(row[1],row[2])
            words.append(row[2])
            etichette.append(row[1])
            line_count += 1


    print(f'Processed {line_count} lines.')



# Create word embeddings
word_embeddings = c2v_model.vectorize_words(words)
print(word_embeddings)
print(len(word_embeddings))



model = SpectralClustering(n_clusters=n_cluster,
             assign_labels="discretize",
             random_state=0).fit(word_embeddings)
labels=model.labels_
print(labels)


generateCSV(labels,etichette)


sys.argv = ['./readClusterData3.py',n_cluster,embedding,'Spectral']

exec(open("./readClusterData3.py").read())



print("eseguito")