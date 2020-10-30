import sys

#Primo parametro numero di cluster, secondo parametro embedding

#for i in range(2,70):
 #  print("ITERAZIONE NUMERO: ",i)
  # sys.argv = ['./kmean_repeatCopia.py',i, '200']
   #exec(open("./kmean_repeatCopia.py").read())



#for i in range(2,70):
 #   print("ITERAZIONE NUMERO: ",i)
  #  sys.argv = ['./gaussianMM_repeat.py',i, '300']
   # exec(open("./gaussianMM_repeat.py").read())


#for i in range(2,70):
 #   print("ITERAZIONE NUMERO: ",i)
  #  sys.argv = ['./BIRCH_repeatCopia.py',i, '50']
   # exec(open("./BIRCH_repeatCopia.py").read())



for i in range(2,70):
    print("ITERAZIONE NUMERO: ",i)
    sys.argv = ['./gaussianMM_repeat2.py',i,'300']
    exec(open("./gaussianMM_repeat2.py").read())
