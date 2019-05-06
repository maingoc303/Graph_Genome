#------------------------------------ PACKAGES ---------------------------------#

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Bio import SeqIO


#---------------------- RUN ALIGNMENT COMMAND FROM GROOT ------------------------#

# simulation
#list_fasta_files = []
input_folder = str(input('Name of folder you want to save all fastq files for running alignment'))
os.system('mkdir '+input_folder)

def simulate(fa_file, N_reads, read_length, mutation_rate, error_rate):
	'''
	this function will simulate the reads to create novo short gun data
	from fasta file by applying wgsim
	input are: fasta file, number of reads, length of read, mutation rate and
	error rate
	'''
	#import os
	path = os.getcwd() 
	os.system('wgsim -R 0 -r '+str(mutation_rate)+' -e '+str(error_rate)+' -N '+ str(N_reads)+' -1 '+str(read_length)+' -2 '+str(read_length)+ ' contamination/'+fa_file+ ' fq_files/'+fa_file.replace('.fa','1.fastq') + ' fq_files/' + fa_file.replace('.fa','2.fastq'))
	os.system('cat fq_files/'+fa_file.replace('.fa','1.fastq') +' '+input_folder + fa_file.replace('.fa','2.fastq')+' > '+input_folder+fa_file.replace('.fa','.fastq'))
	os.system('rm fq_files/'+fa_file.replace('.fa','1.fastq') +' '+input_folder + fa_file.replace('.fa','2.fastq'))

output_folder = str(input('Name of folder you want to save all result after alignment '))+'/'

os.system('mkdir '+ output_folder)

def align(fq_file):
	#import os
	path = os.getcwd()
	os.system('groot align -i groot-index -f fq_files/'+fq_file + ' -o ./graph > '+output_folder+fq_file.replace('.fastq','.bam'))
	os.system('groot report -i '+output_folder+fq_file.replace('.fastq','.bam')+' > '+output_folder+fq_file.replace('.fastq','.csv'))


path=os.getcwd()
file_names = os.listdir(path+'/contamination/')
N_reads = int(input("How many reads will be generated? "))
read_length = int(input("What is read length? "))
mutation_rate = float(input("Mutation rate (decimal number - from 0 to 0.01) in sequences? "))
error_rate = float(input("Error rate (decimal number - from 0 to 0.01) of sequencing procedure? "))

# generate fastq files from fasta files in folder fa_files
for f in file_names:
	simulate(f, N_reads, read_length, mutation_rate, error_rate)



#######
file_names = os.listdir(path+'/fq_files/')
for f in file_names:
	align(f)



os.system('cat ')