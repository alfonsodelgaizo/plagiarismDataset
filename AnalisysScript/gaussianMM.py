from sklearn.mixture import GaussianMixture
import chars2vec
import sklearn.decomposition
import matplotlib.pyplot as plt
import csv

words=[]
etichette=[]

with open('datasetParsing2DEF.csv') as csv_file:
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

gmm = GaussianMixture(n_components=2).fit(word_embeddings)
labels = gmm.predict(word_embeddings)
print(labels)
for j in range(0,len(labels)):
    plt.scatter(word_embeddings[j, 0], word_embeddings[j, 1], label=j, s=3000, cmap='viridis',marker=('$' + etichette[j] + '$'));


plt.show()