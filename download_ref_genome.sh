# Step 1: Download reference genome

# this is first step to download all reference genome for creating cluster database

cd support_files

# extracting accession number from fasta file which contains all reference genome
grep '>' 2019.04.02.enteroviruses_to_align.fa > list_acc_no.txt

# get the first world of each line in file with tab delimited
cut -d' ' -f1 list_acc_no.txt > accession_no.txt

# delete 1st character at first position
sed 's .  ' accession_no.txt > ID.txt

cd ..

mkdir gb_files
while read line; do
	wget -O gb_files/$line.gb "http://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?db=nuccore&dopt=gb&sendto=on&id=$line";
done < support_files/ID.txt


