#Prende in input il nome dell'algo di clustering e leggendo i dati relativi ai risultati
# delle somme delle clusterizzazioni di ogni coppia di canzoni (salvati in Result_General)
# crea un file CSV per ogni coppia (da 0 a 51) .csv in cui vi è la descrizione in termini di percentuale
# della frequenza dei vari algoritmi di clustering nel mettere le canzoni accoppiate negli stessi cluster.
# I file .csv sono contenuti nella cartella Percentage_1 e divisi in path in base all'algo tenuti in considerazione
# Il lavoro è tutto nello script plotPerc.py


import sys

algo='Agglomerative'
for i in range(0,52):
    sys.argv = ['./plotPerc.py',algo,i]
    exec(open("./plotPerc.py").read())