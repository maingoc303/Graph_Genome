import os
from Bio import SeqIO

path = os.getcwd()
msa_folder = '/CLUSTERED-DB/'

files = list(os.walk(path+msa_folder))[0][2]

# create new directory to store clean msa files (remove consensus after run vsearch for clustering)

os.makedirs('no_consensus')

for i in range(len(files)):
    f = open(path+msa_folder+files[i],'r').readlines()
    g = open(path+'/no_consensus/'+files[i],'w')
    for j in range(f.index('>consensus\n')):
        g.write(f[j])
