import chars2vec
import sklearn.decomposition
import matplotlib.pyplot as plt
import csv
from kneed import DataGenerator, KneeLocator

# Load Inutition Engineering pretrained model
# Models names: 'eng_50', 'eng_100', 'eng_150' 'eng_200', 'eng_300'
from sklearn.cluster import KMeans

c2v_model = chars2vec.load_model('eng_100')

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

Sum_of_squared_distances = []
sse=[]
K = range(1,100)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(word_embeddings)
    Sum_of_squared_distances.append(km.inertia_)
    sse.append(km.inertia_)

kl = KneeLocator(
   range(1, 100), sse, curve = "convex", direction = "decreasing"
     )
print("ELBOW:",kl.elbow)


plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.show()


