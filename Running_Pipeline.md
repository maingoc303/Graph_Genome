# User provide the file contain the list of accession_id for building up database

### Set working directory
cd [directory_name]

Create directory to save all support files to run pipeline
mkdir support_files

Save the file with list of accession_id to support_files folder

Create directory for saving all scripts
mkdir script
load all shell and python scripts to this folder

### Running shell script to download all genbank files and save to genbank folder

At current working directory, run shell script
sh script/download_ref_genome.sh

After this script is finished, working directory will have more folders as below:
* gb_files: this folder contains all genbank files downloaded for each of reference genome listed

### Running python script to extract mature peptides of reference genomes
python script/extract_mp.py

After this script, new folder will be created in working directory:
* fna_folder: this folder contains all fna_folder (pre-clustered database). All fna_files in this folder will be indexed to run multiple sequence alignment for clustering 
* combine.fna: this file combines content of all reference genomes

### Running