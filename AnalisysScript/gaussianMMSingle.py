import chars2vec
import sklearn.decomposition
import matplotlib.pyplot as plt
import csv
from sklearn.cluster import KMeans


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

# Load Inutition Engineering pretrained model
# Models names: 'eng_50', 'eng_100', 'eng_150' 'eng_200', 'eng_300'
c2v_model = chars2vec.load_model('eng_50')



# Create word embeddings
word_embeddings = c2v_model.vectorize_words(words)

# Project embeddings on plane using the PCA
projection_2d = sklearn.decomposition.PCA(n_components=10).fit_transform(word_embeddings)


kmeans = KMeans(
              init="random",
             n_clusters=10,
              n_init=10,
              max_iter=300,
             random_state=30)

kmeans.fit(projection_2d),

y_kmeans = kmeans.predict(projection_2d)
print(y_kmeans)
i=0;
for j in range(0,len(y_kmeans)):
    print(etichette[i])
    print(word_embeddings[j,0])
    print(word_embeddings[j,1])
    print()
    #plt.scatter(word_embeddings[:, 0], word_embeddings[:, 1],marker=('$' + etichette[i] + '$'),c=y_kmeans, s=1800)
    plt.scatter(projection_2d[j, 0], projection_2d[j, 1],
                marker=('$' + etichette[i] + '$'),
                s=3000, label=j,
                facecolors='red' if etichette[i]
                                    in ['spider.mxl', 'desert_song.mxl'] else 'black')
    i=i+1



centers = kmeans.cluster_centers_

plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)

plt.show()
