import chars2vec
import sklearn.decomposition
import matplotlib.pyplot as plt
import csv
import random
import sys
# Load Inutition Engineering pretrained model
# Models names: 'eng_50', 'eng_100', 'eng_150' 'eng_200', 'eng_300'
from sklearn.cluster import KMeans

print(sys.argv[2])
print(sys.argv[1])
n_clusterString= sys.argv[1]
n_cluster= int(n_clusterString)
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
label_color_Final= []

words = []
etichette = []
song_Names=[]
song_Strings=[]





def trasformLabelColor(l_cluster):

    for j in range(0, len(song_Names)):
        #ottiene il cluster appartenente alla canzone J-esima
        ind=l_cluster[j]
        coloreEffettivo=label_color[ind]
        label_color_Final.append(coloreEffettivo)



def modificaLabelColor():
    with open('./Results_1/Kmean/'+embedding+'/clusteCoupler'+n_clusterString+'.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                song1=row[1]
                i=0
                for et in range(0,len(song_Names)):
                    if (song1==song_Names[i]):
                        label_color_Final[i]= '#ff0000'
                    i=i+1

                song2=row[2]
                k=0
                for et in range(0, len(song_Names)):
                    if (song2 == song_Names[k]):
                        label_color_Final[k] = '#ff0000'
                    k=k+1

                line_count += 1

        print(f'Processed {line_count} lines.')



def pca(l_cluster):


    with open('datasetParsingDEF.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print( 'WORD' ,row[1][:-4])
                song_Strings.append(row[2])
                song_Names.append(row[1][:-4])
                line_count += 1

        print(f'Processed {line_count} lines.')

    # Load Inutition Engineering pretrained model
    # Models names: 'eng_50', 'eng_100', 'eng_150' 'eng_200', 'eng_300'
    c2v_model = chars2vec.load_model(embedding)

    # Create word embeddings
    word_embeddings = c2v_model.vectorize_words(song_Strings)

    # Project embeddings on plane using the PCA
    projection_2d = sklearn.decomposition.PCA(n_components=2).fit_transform(word_embeddings)

    # Draw words on plane
    f = plt.figure(figsize=(8, 6))
    plt.title("KMean - Divisione : "+n_clusterString+' Cluster - Embedding : '+ embedding)
    #label_color = [LABEL_COLOR_MAP[l] for l in l_cluster]

    print(song_Names)
    trasformLabelColor(l_cluster)
    print(label_color_Final)

    i = 0;

    print(len(l_cluster))

    modificaLabelColor()

    print(label_color_Final)


    for j in range(len(projection_2d)):
        print(j)
        plt.scatter(projection_2d[j, 0], projection_2d[j, 1],
                    marker=('$' + 'o' + '$'),
                    s=30, label=j,
                    c=label_color_Final[j]
                    )
        i = i + 1


    plt.savefig('./Scatter/Kmean/'+embedding+'/'+n_clusterString+'.png')

    #plt.show()




c2v_model = chars2vec.load_model(embedding)



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

for i in range(0,n_cluster+1):
    r = lambda: random.randint(180, 255)
    esadecimale='#%02X%02X%02X' % (r(), r(), r())
    label_color.append(esadecimale)

word_embeddings = c2v_model.vectorize_words(words)
print(word_embeddings)


kmeans = KMeans(
              init="random",
             n_clusters=n_cluster,
              max_iter=500,
             random_state=0)

kmeans.fit(word_embeddings),

y_kmeans = kmeans.predict(word_embeddings)
print(y_kmeans)

#generateCSV(y_kmeans,etichette)

pca(y_kmeans)

#sys.argv = ['./readClusterData.py',n_cluster,embedding,'KMean']

#exec(open("./readClusterData.py").read())



print("eseguito")