import chars2vec
import sklearn.decomposition
import matplotlib.pyplot as plt
import csv
import sys
import random
import plotly.graph_objects as go
import numpy as np

# Load Inutition Engineering pretrained model
# Models names: 'eng_50', 'eng_100', 'eng_150' 'eng_200', 'eng_300'
from plotly.graph_objs import Layout
from sklearn.cluster import KMeans, MiniBatchKMeans, SpectralClustering, AgglomerativeClustering, Birch
from sklearn.mixture import GaussianMixture

algo=sys.argv[1]
n_clusterString=sys.argv[2]
n_cluster= int(n_clusterString)
t_embedding=sys.argv[3]

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
    with open('./Results_1/'+algo+'/'+embedding+'/clusteCoupler'+n_clusterString+'.csv') as csv_file:
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

    print(len(projection_2d))

    assex=[]
    assey=[]

    for j in range(0,len(projection_2d)):
        assex.append(projection_2d[j, 0])
        assey.append(projection_2d[j, 1])



    fig = go.Figure(data=go.Scatter(
        x=assex,
        y=assey,
        mode='markers',
        text=song_Names,
        marker=dict(
            size=16,
            color=label_color_Final,  # set color equal to a variable
            showscale=True,
        )
    ))

    fig.update_xaxes( showgrid=False)
    fig.update_yaxes( showgrid=False)

    fig.update_layout(title_text=algo+'  '+embedding+'  '+n_clusterString,plot_bgcolor='rgb(236,241,243)')

    fig.show()

    for j in range(len(projection_2d)):
        print(j)
        plt.scatter(projection_2d[j, 0], projection_2d[j, 1],
                    marker=('$' + 'o' + '$'),
                    s=30, label=j,
                    c=label_color_Final[j]
                    )
        i = i + 1


    #plt.savefig('./Scatter_1/GaussianMM/'+embedding+'/'+n_clusterString+'.png')



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


if (algo=='Kmean'):
    kmeans = KMeans(
                  init="random",
                 n_clusters=n_cluster,
                  max_iter=500,
                 random_state=0)

    kmeans.fit(word_embeddings),

    y_kmeans = kmeans.predict(word_embeddings)

    #generateCSV(y_kmeans,etichette)

    pca(y_kmeans)


if (algo=='GaussianMM'):
    gmm = GaussianMixture(n_components=n_cluster).fit(word_embeddings)
    labels = gmm.predict(word_embeddings)
    pca(labels)


if (algo=='MiniBatch100'):
    kmeans = MiniBatchKMeans(n_clusters=n_cluster,
                             batch_size=100,
                             ).fit(word_embeddings)

    kmeans.fit(word_embeddings),

    y_kmeans = kmeans.predict(word_embeddings)
    print(y_kmeans)
    pca(y_kmeans)


if (algo=='MiniBatch250'):
    kmeans = MiniBatchKMeans(n_clusters=n_cluster,
                             batch_size=250,
                             ).fit(word_embeddings)

    kmeans.fit(word_embeddings),

    y_kmeans = kmeans.predict(word_embeddings)
    print(y_kmeans)
    pca(y_kmeans)

if (algo=='MiniBatch500'):
    kmeans = MiniBatchKMeans(n_clusters=n_cluster,
                             batch_size=500,
                             ).fit(word_embeddings)

    kmeans.fit(word_embeddings),

    y_kmeans = kmeans.predict(word_embeddings)
    print(y_kmeans)
    pca(y_kmeans)


if (algo=='MiniBatch1000'):
    kmeans = MiniBatchKMeans(n_clusters=n_cluster,
                             batch_size=1000,
                             ).fit(word_embeddings)

    kmeans.fit(word_embeddings),

    y_kmeans = kmeans.predict(word_embeddings)
    print(y_kmeans)
    pca(y_kmeans)

if (algo=='Spectral'):
    clustering = SpectralClustering(n_clusters=n_cluster,
                                    assign_labels="discretize",
                                    random_state=0).fit(word_embeddings)
    labels = clustering.labels_
    print(labels)
    pca(labels)

if(algo=='Agglomerative'):
    cluster = AgglomerativeClustering(n_clusters=n_cluster, affinity='euclidean', linkage='ward')
    cluster.fit_predict(word_embeddings)
    labels = cluster.labels_
    pca(labels)

if(algo=='BIRCH'):
    brc = Birch(n_clusters=n_cluster)
    brc.fit(word_embeddings)
    labels = brc.predict(word_embeddings)
    print(labels)
    pca(labels)

print("eseguito")