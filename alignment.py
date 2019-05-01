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
	path = os.getcwd() + '/fa_files/'
	os.system('wgsim -R 0 -r '+str(mutation_rate)+' -e '+str(error_rate)+' -N '+
		str(N_reads)+' -1 '+str(read_length)+' -2 '+str(read_length)+ ' '+ str(id)
		+ ' '+ str(id)+'_1.fastq'+ ' '+ str(id)+'_2.fastq')

def align(fastq_file):
	import os
	path = os.getcwd() + '/fastq/'
	os.system('groot align -i ' + path +/groot_index/ -f combine1000.fastq > reads1000.bam')


for id in list_fasta_files:
	os.system('wgsim -R 0 -r 0 -e 0 -N 10000 -1 100 -2 100 ../../' + str(id)+ ' '+ str(id)+'_1.fastq'+ ' '+ str(id)+'_2.fastq')