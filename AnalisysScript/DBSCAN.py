import matplotlib.pyplot as plt
import csv
import random
import chars2vec
from sklearn.cluster import Birch, DBSCAN, OPTICS
import sklearn.decomposition


n_cluster=6

label_color = []

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
    c2v_model = chars2vec.load_model('eng_100')

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
    plt.show()



for i in range(0,n_cluster+1):
    r = lambda: random.randint(0, 255)
    esadecimale='#%02X%02X%02X' % (r(), r(), r())
    label_color.append(esadecimale)


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
            print(row[1], row[2])
            words.append(row[2])
            etichette.append(row[1])
            line_count += 1

    print(f'Processed {line_count} lines.')

    # Load Inutition Engineering pretrained model
    # Models names: 'eng_50', 'eng_100', 'eng_150' 'eng_200', 'eng_300'
c2v_model = chars2vec.load_model('eng_50')

# Create word embeddings
word_embedding = c2v_model.vectorize_words(words)
print(word_embedding)
clustering = DBSCAN(eps=1.20, min_samples=4).fit(word_embedding)
labels=clustering.labels_


print(labels)
print("number of labels: ", set(labels))


pca(labels)



