import chars2vec
import sklearn.decomposition
from sklearn.cluster import Birch
import matplotlib.pyplot as plt
import csv
import random
import sys


# Load Inutition Engineering pretrained model
# Models names: 'eng_50', 'eng_100', 'eng_150' 'eng_200', 'eng_300'
from sklearn.cluster import KMeans

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

    with open('cluster2.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['N','Song', 'Cluster'])
        i=0
        for l in labels:
            single_Name = name[i][:-4]
            filewriter.writerow([i,single_Name,l])
            i=i+1

def pca(l_cluster):
    words = []
    etichette = []

    with open('datasetParsingDEF.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(row[1], row[2])
                words.append(row[2])
                etichette.append(row[1])
                line_count += 1

        print(f'Processed {line_count} lines.')

    # Load Inutition Engineering pretrained model
    # Models names: 'eng_50', 'eng_100', 'eng_150' 'eng_200', 'eng_300'
    c2v_model = chars2vec.load_model(embedding)

    # Create word embeddings
    word_embeddings = c2v_model.vectorize_words(words)

    # Project embeddings on plane using the PCA
    projection_2d = sklearn.decomposition.PCA(n_components=2).fit_transform(word_embeddings)

    # Draw words on plane
    f = plt.figure(figsize=(8, 6))

    #label_color = [LABEL_COLOR_MAP[l] for l in l_cluster]

    print(label_color)

    i = 0;

    print(len(l_cluster))

    for j in range(len(projection_2d)):
        print(j)
        plt.scatter(projection_2d[j, 0], projection_2d[j, 1],
                    marker=('$' + 'o' + '$'),
                    s=30, label=j,
                    c=label_color[l_cluster[j]]
                    )
        i = i + 1
    #plt.show()


c2v_model = chars2vec.load_model(embedding)

words=[]
etichette=[]

with open('datasetParsingDEF.csv') as csv_file:
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


brc = Birch(n_clusters=n_cluster)
brc.fit(word_embeddings)
labels=brc.predict(word_embeddings)

print(labels)

generateCSV(labels,etichette)

#pca(labels)

sys.argv = ['./readClusterDataCopia.py',n_cluster,embedding,'BIRCH']

exec(open("./readClusterDataCopia.py").read())



print("eseguito")