#Prende in input il nome dell'algo di clustering e leggendo i dati relativi ai risultati
# delle somme delle clusterizzazioni di ogni coppia di canzoni (salvati in Result_General_2)
# crea un file CSV per ogni coppia (da 0 a 51) .csv in cui vi è la descrizione in termini di percentuale
# della frequenza dei vari algoritmi di clustering nel mettere le canzoni accoppiate negli stessi cluster.
# I file .csv sono contenuti nella cartella Percentage_1 e divisi in path in base all'algo tenuti in considerazione
# Il lavoro è tutto nello script plotPerc2.py


import sys
algoArray=['Agglomerative','BIRCH','Kmean','GaussianMM','Spectral','MiniBatch100','MiniBatch250','MiniBatch500','MiniBatch1000']

for j in algoArray:
  algo=j
  for i in range(0,52):
    sys.argv = ['./plotPerc2.py',algo,i]
    exec(open("./plotPerc2.py").read())