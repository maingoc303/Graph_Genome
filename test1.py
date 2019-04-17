import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

from bokeh.io import output_notebook, show
from bokeh.plotting import figure

l=[]
id_range=np.arange(0.1,1,0.1)
df=pd.DataFrame(np.zeros(shape=(len(id_range),7)),columns=['id','clust_no','max_size','min_size','avg_size','no_clust_all_genome','no_prot_in_multi'])
for i in range(len(id_range)):
   id = id_range[i]
   df['id'][i] = id
   os.system('vsearch --cluster_size combine.fna --id '+str(id)+' --clusters STRING --log t.txt')
   f = open('t.txt', 'r').readlines()
   l.append(f[-7])
   x=f[-7].split(' ')
   df['clust_no'][i]=x[1]
   df['max_size'][i]=int(x[6][:-1])
   df['min_size'][i]=int(x[4][:-1])
   df['avg_size'][i]=float(x[-1][:-1])
   # remove all cluster files extracted
   os.system("grep '>' STRING* > protein_name.txt")
   ############################## Dealing with data ################################
   data = pd.read_csv("protein_name.txt", delimiter=':>', engine='python',
                      header=None, names=['cluster', 'protein'])
   # dropping null value columns to avoid errors
   data.dropna(inplace=True)
   # new data frame with split value columns
   new = data["protein"].str.split("_", n=1, expand=True)
   # making seperate first name column from new data frame
   data["accession_no"] = new[0]
   # making seperate last name column from new data frame
   data["prot"] = new[1]
   # Dropping old Name columns
   data.drop(columns=["protein"], inplace=True)
   # create new column for checking prot from genome in cluster
   data['unique'] = data['accession_no'] + '_' + data['prot']
   unique = pd.crosstab(data['unique'], data['cluster'], margins=False)
   # How many clusters have exactly one protein from every genome
   clust = pd.crosstab(data['accession_no'], data['cluster'], margins=False)
   df['no_clust_all_genome'][i] = int(sum(clust.sum(axis=0)>=clust.shape[0]))
   # How many protein are assigned in more than 1 cluster
   unique = pd.crosstab(data['unique'], data['cluster'], margins=False)
   # unique.sum(axis=1)
   x = pd.DataFrame(unique)
   x['test'] = unique.sum(axis=1)
   df['no_prot_in_multi'][i]=int(sum(x['test']>1))
   # remove file protein_name.txt for next loop
   os.system('rm STRING*')
   # os.system('rm protein_name.txt')

output_file("test.html")

# create a new plot with default tools, using figure
p = figure(plot_width=400, plot_height=400)

# add a circle renderer with x and y coordinates, size, color, and alpha
p.circle(df['id'], df['clust_no'], size=15, line_color="navy", fill_color="orange", fill_alpha=0.5)

show(p)
