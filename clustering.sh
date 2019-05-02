# this is step 3: runing vsearch to cluster genes (mature peptides) based on identity percentage
# output is the cluster database for alignment raw reads (fastq files) from Illimina platform
# for detecting which pathogen presents in the samples (depend on library, only pathogen that is
# included in library is detected, cannot identify unknown pathogen now)

# this bash script is run with identity percentage = 50% and all cluster (saved under .msa format)
# will be saved in folder Cluster-DB

# list of msa file for indexing
mkdir MSA-DB && cd $_

vsearch --cluster_size ../combine.fna --id 0.50 --msaout MSA.tmp

awk '!a[$0]++ {of="./cluster-" ++fc ".msa"; print $0 >> of ; close(of)}' RS= ORS="\n\n" MSA.tmp && rm MSA.tmp

cd ..


# index Cluster database for building graph, this command will access all msa files in folder MSA
# before indexing database, remove all consensus sequences in each of msa files by running python 
# script, this script will remove all consensus sequences and save all new msa files to folder no_consensus
mkdir no_consensus
python clean_consensus.py

# replace . in accession ID with "_":
sed -i 's/\./\""/g' no_consensus/*.msa

# remove duplicate sequences


# indexing database 
groot index -i ./no_consensus -o groot-index -l 100

# create folder for containing Cluster info
# mkdir Cluster-DB

# vsearch --cluster_size combine.fna --id 0.5 --clusters Cluster-DB/Cluster 


