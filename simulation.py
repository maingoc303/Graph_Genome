# packages
import os
import pandas as pd
import numpy as np
import csv
from Bio import SeqIO

# this script will generate sample with fastq files based on parameters input: number of reads, read length, error rate and mutation rate



# download all fasta files and save to folder fa_files
mkdir fa_files

# list of reference genome (accession_id) is contain in text file fa_files.txt
cat support_files/ID.txt support_files/contam.txt > support_files/fa_files.txt

while read line; do
	wget -O fa_files/$line.fasta "http://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?db=nuccore&dopt=gb&sendto=on&id=$line";
done < support_files/fa_files.txt

# simulating each of fasta files to 2 fastq files by wsim command and save to fq_files folder
mkdir fq_files








