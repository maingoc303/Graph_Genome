import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import os

data = pd.read_csv("/home/ubuntu/graph_genomes/data/2019.04.12/protein_name.txt",delimiter=':>',engine='python',header=None,names=['cluster','protein'])

# dropping null value columns to avoid errors
data.dropna(inplace = True)

# new data frame with split value columns
new = data["protein"].str.split("_", n = 1, expand = True)

# making seperate first name column from new data frame
data["accession_no"] = new[0]

# making seperate last name column from new data frame
data["prot"] = new[1]

# Dropping old Name columns
data.drop(columns=["protein"], inplace=True)

# create new column for checking prot from genome in cluster
data['unique']=data['accession_no']+'_'+data['prot']

unique = pd.crosstab(data['unique'],
                            data['cluster'],
                                margins = False)

# How many clusters there are

df=pd.DataFrame(pd.crosstab(data['cluster'],data['accession_no']))
print('\n 1. There are %i clusters' % df.shape[0])

# How big is the average cluster

# p1=df.plot(kind="bar",figsize=(8,8),stacked=True)

no_prot_in_clust = pd.crosstab(data['cluster'],
                            data['prot'],
                                margins = False)
prot = pd.DataFrame(no_prot_in_clust)
prot['sum']=no_prot_in_clust.sum(axis=1)
print('\n 2. Number of protein in each cluster:')
print(prot['sum'])

# p2=prot.plot(kind="bar",figsize=(10,8),stacked=True)

clust = pd.crosstab(data['accession_no'],
                            data['cluster'],
                                margins = False)
# p3=clust.plot(kind="bar",figsize=(10,11),stacked=True)

# How many clusters have exactly one protein from every genome
print("\n 3. There are %i clusters have exactly one protein from every genome" % sum(clust.sum(axis=0)==clust.shape[0]))

multi_clust = pd.crosstab(data['prot'],
                            data['cluster'],
                                margins = False)
# p4=multi_clust.plot(kind="bar",figsize=(10,10),stacked=True)

unique = pd.crosstab(data['unique'],
                            data['cluster'],
                                margins = False)

#unique.sum(axis=1)
x=pd.DataFrame(unique)

x['test']=unique.sum(axis=1)
print('\n 4. %i proteins are in multiple cluster' % sum(x['test']>1))
