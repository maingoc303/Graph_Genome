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
+ Raw reads in fastq files are trimmed out by FastQC with default Q = 20
+ Visualisation of number of reads before and after quality check can be provided

### Alignment reads

### Building graph
+ Multiple reference graph is visualised by Bandage

## Cluster Analysis
### List of metrics

### Visualisation

### 
