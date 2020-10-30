import sys

#algo='Agglomerative'
for i in range(2,70):
    n_cluster=str(i)
    sys.argv = ['./riduction_GaussianMM.py',n_cluster,'50']
    exec(open('./riduction_GaussianMM.py').read())