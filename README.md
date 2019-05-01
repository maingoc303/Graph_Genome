# Graph_Genome
## Introduction
This pipeline is developed for detecting rare pathogens by aligning raw reads from Illumina platform to graph reference genome. This graph based approach allows to use multiple reference genome in sequencing. Currently, this pipeline is developed for detecting subtypes of Enterovirus species.

Vsearch algorithm is used to cluster matured peptides of all known subtypes of Enterovirus.

Groot Graphs is used to index database for searching and build graph for visualizing the variants between all subtypes within Enterovirus species.

## Pipeline 
### Building Clustering Database
+ Fasta file including all known subtypes is provided.
+ From this fasta file, obtain the list of accession_no for each subtype then download genbank files contain completem genome for each subtype
+ Extract matured peptides of each subtypes and prepare pre-clustered files (under format '*.fna')
+ Run *vsearch* to get the clustered database
+ Index the database for building graph by running *groot*
### Fastq file processing
+ Raw reads in fastq files are trimmed out by FastQC with default Q = 20, this will be changed after testing for TP,FP,TN,FN
+ Visualisation of number of reads before and after quality check can be provided

### Alignment reads
After multiple sequence alignment database is built up, alignment reads from fastq files can be started with shell script to run python script, a table result for read alignment is extracted with information include:

### Building graph
+ Multiple reference graph is visualised by Bandage

## Cluster Analysis
### List of metrics

### Visualisation
Graph genome is visualised by Bandage to get the overview about variation, hitting when aligning the query sequence.

## Simulation data
Simulated fastq files will be created from fasta files:
  * simulation for the read length
  * simulation for the error rate
  * simulation for the contaminat reads
  * simulation for ...

### Estimating the FDR
#### One query sample versus graph

#### Multiple query samples versus graph

#### Adding mutation rate to query samples

### Estimated sensitivity and specificity
#### Estimating TP and FN

#### Estimating FP and TN

#### Calculating sensitivity and specificity
