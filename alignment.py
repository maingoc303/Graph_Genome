#------------------------------------ PACKAGES ---------------------------------#

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Bio import SeqIO


#---------------------- RUN ALIGNMENT COMMAND FROM GROOT ------------------------#

# simulation
list_fasta_files = []

def simulate(fa_file, N_reads, read_length, mutation_rate, error_rate):
	'''
	this function will simulate the reads to create novo short gun data
	from fasta file by applying wgsim
	input are: fasta file, number of reads, length of read, mutation rate and
	error rate
	'''
	import os
	path = os.getcwd() + '/'#fa_files/'
	os.system('wgsim -R 0 -r '+str(mutation_rate)+' -e '+str(error_rate)+' -N '+
		str(N_reads)+' -1 '+str(read_length)+' -2 '+str(read_length)+ ' '+path
		+fa_file+ fa_file.replace('.fa','1.fastq') + ' ' + fa_file.replace('.fa','2.fastq'))

def align(fastq_file):
	import os
	path = os.getcwd()
	os.system('groot align -i ' + path +'/groot_index/ -f ' + fastq_file + ' > output.bam')
	os.system('groot report -i output.bam > output.csv')



file_names = os.listdir('fa_files/')
N_reads = int(input("How many reads will be generated? "))
read_length = int(input("What is read length? "))
mutation_rate = float(input("Mutation rate (decimal number - from 0 to 0.01) in sequences? "))
error_rate = float(input("Error rate (decimal number - from 0 to 0.01) of sequencing procedure? "))

# generate fastq files from fasta files in folder fa_files
for f in file_names:
	simulate(f, N_reads, read_length, mutation_rate, error_rate)