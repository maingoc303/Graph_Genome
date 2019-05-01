import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as mpl
from Bio import SeqIO

# import other python file
import extract_mp as mp


d = dict()
for i in mp.access_vs_no_prot.keys():
    d[i.replace(".","")] = mp.access_vs_no_prot[i]
# function
def alignment_report(f,d):
	alignment_result = pd.read_csv(f,sep="\t",names=["gene","read_count","read_length","coverage"])
	tot_prot = list()
	for i in range(len(alignment_result["gene"])):
		tot_prot.append(d[alignment_result["gene"][i][:alignment_result["gene"][i].index("_")]])
	alignment_result["tot_prot"] = tot_prot
	# split gene name in table above to accession_no and protein name
	# dropping null value columns to avoid errors
	alignment_result.dropna(inplace=True)
	# new data frame with split value columns
	new = alignment_result["gene"].str.split("_", n=1, expand=True)
	# making seperate first name column from new data frame
	alignment_result["accession_no"] = new[0]
	# making seperate last name column from new data frame
	alignment_result["prot"] = new[1]
	# Dropping old Name columns, should not, however, this info can obtain from 1st row, "gene"
	# alignment_result.drop(columns=["protein"], inplace=True)
	return alignment_result



############ report ################
def search_each_ref_genome(f,d):
	t = alignment_report(f,d)
	pd.DataFrame.to_html
	report1 = pd.crosstab(t["accession_no"],t["prot"],margins=True,aggfunc=t["prot"])

np.su

pd.crosstab(data['unique'], data['cluster'], margins=False)



alignment_result = pd.read_csv("bam_report.csv",sep="\t",names=["gene","read_count","read_length","coverage"])

for i in range(len(alignment_result["gene"])):
	alignment_result["tot_prot"][i]=access_vs_no_prot[alignment_result["gene"][i]]


# split gene name in table above to accession_no and protein name
# dropping null value columns to avoid errors
alignment_result.dropna(inplace=True)
# new data frame with split value columns
new = alignment_result["gene"].str.split("_", n=1, expand=True)
# making seperate first name column from new data frame
alignment_result["accession_no"] = new[0]
# making seperate last name column from new data frame
alignment_result["prot"] = new[1]
# Dropping old Name columns, should not
alignment_result.drop(columns=["protein"], inplace=True)

# extract csv file for table above




