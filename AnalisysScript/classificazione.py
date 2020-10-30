import chars2vec

dim = 50



X_train = [('p-8111-20p-4-417-20p-35-200-24-5-2-222p3-8111-2-4', 'p000-3002000-400-35-20-20p-52'), # similar words, target is equal 0
           ('1p1-2-1-1-1-110311-2-3-445-200-1-1-1-113-1-1-15-500-2-2-1-3150212-2-1-422-20212-2-11-8340p', 'p-1p3-2-1-1-2100-12-1-1-1-310-112214-2-13-2-52212-112-2-4-1-25-13-2-1-1-2100-12-1-1-1-31'), # similar words, target is equal 0
           ('52p1-1-20-112-52p-410-2-10-221-1-2p-512-2-20221-1-2021-1-12435-2-3-2-5521-1-20-112-52p-410-2-10-221-1-2p-512-2-20221-1-2021-1-12435-2-2-3p', '22p1225-2-3-2-5p05-2-1127-2-511p-9221225-2-3-2-5p122-2-2-1-1-3-5210p-11221-1-2-2-13-2p-1111-58-1-2-2-1p-4221225-2-3-2-5p122-2-2-1-1-3-5210p') # similar words, target is equal 0

          ]

y_train = [0, 0, 0]

model_chars = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.',
               '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<',
               '=', '>', '?', '@', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
               'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
               'x', 'y', 'z']

# Create and train chars2vec model using given training data
my_c2v_model = chars2vec.train_model(dim, X_train, y_train, model_chars)



words = ['list', 'of', 'words']

# Load pretrained model, create word embeddings
word_embeddings = my_c2v_model.vectorize_words(words)

