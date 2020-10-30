from time import time
import numpy as np
import matplotlib.pyplot as plt
import chars2vec

from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

np.random.seed(42)

X_digits, y_digits = load_digits(return_X_y=True)


c2v_model = chars2vec.load_model('eng_300')

words = ['p-8111-20p-4-417-20p-35-200-24-5-2-222p3-8111-2-4','p000-3002000-400-35-20-20p-52','1p1-2-1-1-1-110311-2-3-445-200-1-1-1-113-1-1-15-500-2-2-1-3150212-2-1-422-20212-2-11-8340p',
'p-1p3-2-1-1-2100-12-1-1-1-310-112214-2-13-2-52212-112-2-4-1-25-13-2-1-1-2100-12-1-1-1-31','52p1-1-20-112-52p-410-2-10-221-1-2p-512-2-20221-1-2021-1-12435-2-3-2-5521-1-20-112-52p-410-2-10-221-1-2p-512-2-20221-1-2021-1-12435-2-2-3p',
         '22p1225-2-3-2-5p05-2-1127-2-511p-9221225-2-3-2-5p122-2-2-1-1-3-5210p-11221-1-2-2-13-2p-1111-58-1-2-2-1p-4221225-2-3-2-5p122-2-2-1-1-3-5210p',
         '30-743-330-2-10-44-2-24-2p002-4-101p5040-2-2-33-1-22p012-7225030-1-2-44-2-24030-1-2-4040-2-24-29-4-5-2-130-37-2-20-2-35-2-10-2-310',
         '30p0-3300-30-2p002p1040-2-2-1p0122030-1-20-2p-335-1-2-20-2-32p','p2-2-5-35-11-5352-2-5220p-4p0p5-834-2-50p035-834-2-40p0-1-2-1-11-3220300-3-115-3-2-1-1',
         '-1-2-22-2-7220032-442-47-2p-808-834-2-50035-834-2-40-11p9000-2-1037-10342','p-110-1-2-22-220-2-2-11-110-1-2-277000-1-2-22-220-2-2-22-220-2-1-27p3-110-1-2-22-220-2-2-11-110-1-2-29',
         'p5-11-11-110-1-2-22-22-220-2-2-11-101-1-2-270p25-22-22-220-2-1-22-22-220-2-222-2-220-42p05-11-11-110-1-2-22-22-220-20-2-11-11-1-2-270',
         'p30-20-10-221-63p30-10-20-222-53p30-10-2021-33-10p500080-10-20-20-1-730090-20-20-1-2-2-332050-20-10-2-2-24-20p2p08-10-20-20-1-73p09-20-20-1-2-2-31p-321-3-20p',
         'p-1212-20-1-200-27p-129-20-20-10-22p-422141p4p-122p-422122'
         ]

data = c2v_model.vectorize_words(words)


n_samples, n_features = data.shape
n_digits = len(np.unique(y_digits))
labels = y_digits

sample_size = 300

print("n_digits: %d, \t n_samples %d, \t n_features %d"
      % (n_digits, n_samples, n_features))


print(82 * '_')
print('init\t\ttime\tinertia\thomo\tcompl\tv-meas\tARI\tAMI\tsilhouette')


def bench_k_means(estimator, name, data):
    t0 = time()
    estimator.fit(data)
    print('%-9s\t%.2fs\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'
          % (name, (time() - t0), estimator.inertia_,
             metrics.homogeneity_score(labels, estimator.labels_),
             metrics.completeness_score(labels, estimator.labels_),
             metrics.v_measure_score(labels, estimator.labels_),
             metrics.adjusted_rand_score(labels, estimator.labels_),
             metrics.adjusted_mutual_info_score(labels,  estimator.labels_),
             metrics.silhouette_score(data, estimator.labels_,
                                      metric='euclidean',
                                      sample_size=sample_size)))

bench_k_means(KMeans(init='k-means++', n_clusters=n_digits, n_init=10),
              name="k-means++", data=data)

bench_k_means(KMeans(init='random', n_clusters=n_digits, n_init=10),
              name="random", data=data)

# in this case the seeding of the centers is deterministic, hence we run the
# kmeans algorithm only once with n_init=1
pca = PCA(n_components=n_digits).fit(data)
bench_k_means(KMeans(init=pca.components_, n_clusters=n_digits, n_init=1),
              name="PCA-based",
              data=data)
print(82 * '_')

# #############################################################################
# Visualize the results on PCA-reduced data

reduced_data = PCA(n_components=2).fit_transform(data)
kmeans = KMeans(init='k-means++', n_clusters=n_digits, n_init=10)
kmeans.fit(reduced_data)

# Step size of the mesh. Decrease to increase the quality of the VQ.
h = .02     # point in the mesh [x_min, x_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will assign a color to each
x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtain labels for each point in mesh. Use last trained model.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(1)
plt.clf()
plt.imshow(Z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()),
           cmap=plt.cm.Paired,
           aspect='auto', origin='lower')

plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
# Plot the centroids as a white X
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1],
            marker='x', s=169, linewidths=3,
            color='w', zorder=10)
plt.title('K-means clustering on the digits dataset (PCA-reduced data)\n'
          'Centroids are marked with white cross')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()