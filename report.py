# -*- coding: utf-8 -*-
"""
This is script file for generating output after running alignment
fastq files (raw read) to genome graph
"""

from Bio import SeqIO
import pandas as pd
import os
import csv


path=os.getcwd()

# read csv file that contain number of protein per species in support_files folder

#file = path+'/support_files/access_vs_prot.csv'
#with open(file) as fh:
#    rd = csv.DictReader(fh, delimiter=',') 

# create data frame and the split gene column to accession_id and protein name
report = pd.read_csv("test.csv",sep="\t",names=['gene',"read_count","length","coverage"])

# dropping null value columns to avoid errors
report.dropna(inplace = True)

# new data frame with split value columns
new = report["gene"].str.split("_", n = 1, expand = True)

# making seperate first name column from new data frame
report["accession_id"] = new[0]

# making seperate last name column from new data frame
report["prot"] = new[1]

# dictionary to get number of mature peptides extracted for each species
acc_no_vs_prot = pd.read_csv("access_vs_prot.csv",sep=",",names=[''])

acc_no_vs_prot.head()

d = acc_no_vs_prot.to_dict()['']

total_prot = []

for i in report['accession_id']:
  total_prot.append(d[i])

report['total_prot'] = total_prot

table1 = pd.crosstab(report['accession_id'],report['accession_id'],margins=True)










