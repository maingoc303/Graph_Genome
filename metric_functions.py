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
	#print(prot['sum'])
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

def prot_in_multi_clust(dataframe):
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