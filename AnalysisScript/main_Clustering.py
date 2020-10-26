import sys


#Primo parametro numero di cluster, secondo parametro embedding

#for i in range(2,70):
 #  print("ITERAZIONE NUMERO: ",i)
  # sys.argv = ['./kmean_repeat2.py',i, '300']
   #exec(open("./kmean_repeat2.py").read())


#for i in range(2,70):
 #   print("ITERAZIONE NUMERO: ",i)
  #  sys.argv = ['./gaussianMM_repeat.py',i, '300']
   # exec(open("./gaussianMM_repeat.py").read())


#for i in range(2,70):
 #   print("ITERAZIONE NUMERO: ",i)
  #  sys.argv = ['./BIRCH_repeat2.py',i, '300']
   # exec(open("./BIRCH_repeat2.py").read())

for i in range(2,70):
    print("ITERAZIONE NUMERO: ",i)
    sys.argv = ['./miniBatch_repeat2.py',i, '300']
    exec(open("./miniBatch_repeat2.py").read())


#for i in range(2,70):
 # print("ITERAZIONE NUMERO: ",i)
 # print("ITERAZIONE NUMERO: ",i)
  #sys.argv = ['./Agglomerative_repeat2.py',i, '300']
  #exec(open("./Agglomerative_repeat2.py").read())