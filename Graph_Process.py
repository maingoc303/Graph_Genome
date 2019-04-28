def protein_list(id):
	'''
	this function return the text file contain the list of 
	protein of each genome
	input is identity % for clustering lead to location where 
	output of cluster extracted
	'''
	import os
	# run vsearch to get output of each cluster
	os.system('vsearch --cluster_size combine.fna --id '+str(id)+' --clusters Cluster')
	# extract file for list of protein in cluster
	prot_list = os.system('grep '>' Cluster* > protein_name.txt')
	# delete all Cluster extracted:
	os.system('rm Cluster*')
	return prot_list

f =  protein_list(0.5) # input identity % for clustering mature peptides

def clust_info(f):
	'''
	f input is text file contain the list of protein name of each
	genome
	this function return the dataframe with 3 columns: accession_no,
	protein names and cluster that protein belongs
	'''
	import pandas as pd
	data = pd.read_csv(f, delimiter=':>', engine='python',
                      header=None, names=['cluster', 'protein'])
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
	# return dataframe
	return data

def no_clust(dataframe):
	import pandas as pd
	'''
	This function will answers 4 questions about important metrics
	after clustering mature peptides from genome of all known subtypes
	'''
	# Q1: How many clusters there are
	df=pd.DataFrame(pd.crosstab(dataframe['cluster'],dataframe['accession_no']))
	print('\n 1. There are %i clusters' % df.shape[0])
	return df.shape[0]

def size_clust(dataframe):	
	import pandas as pd
	# Q2: How big is each cluster is? (number of protein in each cluster)
	no_prot_in_clust = pd.crosstab(dataframe['cluster'],
                            dataframe['prot'],
                                margins = False)
	prot = pd.DataFrame(no_prot_in_clust)
	prot['sum']=no_prot_in_clust.sum(axis=1)
	print('\n 2. Number of protein in each cluster:')
	print(prot['sum'])
	return prot['sum']

def clust_icl_all_prot(dataframe):	
	import pandas as pd
	# Q3: How many clusters have exactly one protein from every genome
	clust = pd.crosstab(dataframe['accession_no'],
                            dataframe['cluster'],
                                margins = False)
	i = sum(clust.sum(axis=0)==clust.shape[0])
	print("\n 3. There are %i clusters have exactly one protein from every genome" % i)
	print(clust)

def prot_in_multi_clust(dataframe)
	import pandas as pd
	# Q4: How many proteins are in multiple cluster?
	# create new column for checking prot from genome in cluster
	dataframe['unique']=dataframe['accession_no']+'_'+dataframe['prot']
	unique = pd.crosstab(dataframe['unique'],
                            dataframe['cluster'],
                                margins = False)
	multi = pd.DataFrame(unique)
	multi['sum'] = unique.sum(axis=1)
	print('\n 4. %i proteins are in multiple cluster' % sum(multi['sum']>1))
	return sum(multi['sum']>1)

def visual(dataframe):
	from bokeh.io import output, show
	from bokeh.plotting import figure
