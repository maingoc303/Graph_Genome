# download and save file under other name
wget -o [name] [links]

efetch -db GEnbank/GB -a -format -f -id AY421768 > AY421768.1.gb

# convert xls to csv
in2csv samples.xlsx > samples.csv

# use fastq-dump to download the sequence data from accession table
cut -f 1 samples.txt | parallel --gnu "fastq-dump {}"

# extract column from file, d for deliminator
cut -f [column no.] -d '' samples.txt > test.txt

# delete header (first line)
echo "$(tail -n +2 test.txt)" > test.txt

# keep odd lines 
sed 'n; d' infile > outfile

# merge 2 column 
awk -v OFS='' '{print $1,$2}' test.txt > sample.txt

# extract specific row and add to new file
head -1 [current file] >> [new file]

# use vsearch to cluster sequencing by % identity 90% then make a msa output file
vsearch --cluster_size /home/ubuntu/graph_genomes/data/2019.04.03/Test_Align/AY421767.fna --id 0.90 --msaout MSA.tmp

awk '!a[$0]++ {of="./cluster-" ++fc ".msa"; print $0 >> of ; close(of)}' RS= ORS="\n\n" MSA.tmp && rm MSA.tmp

cd .. # this command to comeback previous folder

# combine all files to 1 file
cat *.fna > combine.fna



# Generate resistome profiles
ls *.bam | parallel --gnu "groot report -i {} -c 1 --plotCov > {/.}.report" # -c 1 here to covered by reads with 100% identity match, adjust smaller identity -> 0 to 1


# get the first word of each line in file with tab deliminated
cut -d' ' -f1 list_acc_no.txt

# delete 1 character at first position
sed 's .  ' accession_no.txt   # 1 dot = 1 character


# download file by accession number from file:

wget -O [accession_no].gb "http://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?db=nuccore&dopt=gb&sendto=on&id=[]accession_no]"

# replace dot with underscore
sed -i 's/\./\_/g' cluster*

# simulation data with mutation rate/ error rate
wgsim -e 0 -N 100000 -1 100 -2 100 -r 0 -R 0


# alignment
groot align -i test-index -f EVA90_1.fastq -p 8 > EVA90_1-reads.bam
groot align -i index -f combine.fastq -p 8 > reads1.bam

groot align -i ../../groot_index/ -f EVA90_1.fastq > eva90_vs_all-no-consensus-index.bam

groot report -i *.bam



# simulation reads with mutation rate and error rate
wgsim -R 0 -r 0.1 -e 0 -N 100000 -1 100 -2 100 ../../CVA10.fa CVA10_e1.fastq CVA10_e2.fastq

# then aligning the reads for each rate level of error/mutation to define how many 
# mature peptide can be detected and at how much rate is, there is no detection

## align 1 by 1 query sequence
groot align -i ../../groot_index/ -f EVA90_1.fastq > eva90_vs_all-no-consensus-index.bam

## mix all subtypes to fastq file and alignment
groot align -i index -f combine.fastq -p 8 > reads1.bam

## obtain result for each alignment
groot report -i [].bam > table_of_detection.txt


######################################################################################################################
#							TESTING WITH ABUNDANCE AT 1000 READS WITH ERROR RATE = 0								 #
######################################################################################################################

wgsim -R 0 -r 0 -e 0 -N 1000 -1 100 -2 100 ../../AJ295200.1.fa t1.fastq t2.fastq
wgsim -R 0 -r 0 -e 0 -N 1000 -1 100 -2 100 ../../CVA10.fa t3.fastq t4.fastq
wgsim -R 0 -r 0 -e 0 -N 1000 -1 100 -2 100 ../../CVA03.fa t5.fastq t5.fastq
wgsim -R 0 -r 0 -e 0 -N 1000 -1 100 -2 100 ../../EVA90.fa t7.fastq t8.fastq

cat t1.fastq t2.fastq t3.fastq t4.fastq t5.fastq t6.fastq t7.fastq t8.fastq > combine1000.fastq
groot align -i ../../groot_index/ -f combine1000.fastq > reads1000.bam
groot report -i reads1000.bam

#	AY4217611_VP2   229     765     765M
#	AY6974601_1C    222     732     1D717M14D
#	AY4217611_VP4   18      207     4D201M2D
#	AY4217611_2B    76      297     4D293M
#	AY4217611_2C    314     987     2D984M1D
#	AY4217611_VP3   236     720     5D715M
#	AY6974601_1D    268     885     881M4D
#	AY4217611_3D    453     1386    1386M
#	AY4217611_3A    96      258     258M
#	AY6974601_2A    111     450     9D441M
#	AY6974601_1B    206     765     1D764M
#	AY4217611_2A    134     450     3D446M1D
#	AY4217611_VP1   260     882     2D879M1D
#	AY6974601_2C    320     987     2D979M6D


######################################################################################################################
#					TESTING WITH ABUNDANCE AT 1000 READS WITH ERROR RATE = 1%, MUTATION RATE = 0.1%					 #
######################################################################################################################

wgsim -R 0 -r 0.001 -e 0.01 -N 1000 -1 100 -2 100 ../../AJ295200.1.fa t1.fastq t2.fastq
wgsim -R 0 -r 0.001 -e 0.01 -N 1000 -1 100 -2 100 ../../CVA10.fa t3.fastq t4.fastq
wgsim -R 0 -r 0.001 -e 0.01 -N 1000 -1 100 -2 100 ../../CVA03.fa t5.fastq t5.fastq
wgsim -R 0 -r 0.001 -e 0.01 -N 1000 -1 100 -2 100 ../../EVA90.fa t7.fastq t8.fastq

cat t1.fastq t2.fastq t3.fastq t4.fastq t5.fastq t6.fastq t7.fastq t8.fastq > combine1000werr.fastq
groot align -i ../../groot_index/ -f combine1000werr.fastq > reads1000werr.bam
groot report -i reads1000werr.bam

#	AY4217611_VP1   164     882     2D879M1D
#	AY6974601_2B    17      297     296M1D
#	AY4217611_3A    50      258     258M
#	AY4217611_3D    288     1386    1386M
#	AY4217611_VP2   137     765     3D762M
#	AY4217611_3C    149     549     9D534M6D
#	AY4217611_2C    207     987     2D961M24D
#	AY6974601_1D    104     885     1D879M5D
#	AY6974601_1C    76      732     5D727M
#	AY4217611_VP3   181     720     5D715M
#	AY4217611_2A    90      450     6D444M


######################################################################################################################
#					TESTING WITH ABUNDANCE AT 1000 READS WITH ERROR RATE = 5%, MUTATION RATE = 0.1%					 #
######################################################################################################################

wgsim -R 0 -r 0.001 -e 0.05 -N 1000 -1 100 -2 100 ../../AJ295200.1.fa t1.fastq t2.fastq
wgsim -R 0 -r 0.001 -e 0.05 -N 1000 -1 100 -2 100 ../../CVA10.fa t3.fastq t4.fastq
wgsim -R 0 -r 0.001 -e 0.05 -N 1000 -1 100 -2 100 ../../CVA03.fa t5.fastq t5.fastq
wgsim -R 0 -r 0.001 -e 0.05 -N 1000 -1 100 -2 100 ../../EVA90.fa t7.fastq t8.fastq

cat t1.fastq t2.fastq t3.fastq t4.fastq t5.fastq t6.fastq t7.fastq t8.fastq > combine1000werr5.fastq
groot align -i ../../groot_index/ -f combine1000werr.fastq > reads1000werr5.bam
groot report -i reads1000werr5.bam

#	AY4217611_3C    149     549     9D534M6D
#	AY6974601_2B    17      297     296M1D
#	AY4217611_3A    50      258     258M
#	AY6974601_1C    76      732     5D727M
#	AY4217611_VP1   164     882     2D879M1D
#	AY4217611_VP2   137     765     3D762M
#	AY6974601_1D    104     885     1D879M5D
#	AY4217611_3D    288     1386    1386M
#	AY4217611_VP3   181     720     5D715M
#	AY4217611_2A    90      450     6D444M
#	AY4217611_2C    207     987     2D961M24D

######################################################################################################################
#					TESTING WITH ABUNDANCE AT 1000 READS WITH ERROR RATE = 5%, MUTATION RATE = 0.1%					 #
######################################################################################################################

wgsim -R 0 -r 0.01 -e 0.05 -N 1000 -1 100 -2 100 ../../AJ295200.1.fa t1.fastq t2.fastq
wgsim -R 0 -r 0.01 -e 0.05 -N 1000 -1 100 -2 100 ../../CVA10.fa t3.fastq t4.fastq
wgsim -R 0 -r 0.01 -e 0.05 -N 1000 -1 100 -2 100 ../../CVA03.fa t5.fastq t5.fastq
wgsim -R 0 -r 0.01 -e 0.05 -N 1000 -1 100 -2 100 ../../EVA90.fa t7.fastq t8.fastq

cat t1.fastq t2.fastq t3.fastq t4.fastq t5.fastq t6.fastq t7.fastq t8.fastq > combine1000wm1e5.fastq
groot align -i ../../groot_index/ -f combine1000werr.fastq > reads1000wm1e5.bam
groot report -i reads1000wm1e5.bam

#	AY4217611_2C    207     987     2D961M24D
#	AY4217611_VP2   137     765     3D762M
#	AY4217611_3A    50      258     258M
#	AY6974601_2B    17      297     296M1D
#	AY4217611_2A    90      450     6D444M
#	AY6974601_1C    76      732     5D727M
#	AY6974601_1D    104     885     1D879M5D
#	AY4217611_3D    288     1386    1386M
#	AY4217611_VP1   164     882     2D879M1D
#	AY4217611_3C    149     549     9D534M6D
#	AY4217611_VP3   181     720     5D715M

######################################################################################################################
#					TESTING WITH ABUNDANCE AT 1000 READS WITH ERROR RATE = 1%, MUTATION RATE = 1%					 #
######################################################################################################################

wgsim -R 0 -r 0.01 -e 0.01 -N 1000 -1 100 -2 100 ../../AJ295200.1.fa t1.fastq t2.fastq
wgsim -R 0 -r 0.01 -e 0.01 -N 1000 -1 100 -2 100 ../../CVA10.fa t3.fastq t4.fastq
wgsim -R 0 -r 0.01 -e 0.01 -N 1000 -1 100 -2 100 ../../CVA03.fa t5.fastq t5.fastq
wgsim -R 0 -r 0.01 -e 0.01 -N 1000 -1 100 -2 100 ../../EVA90.fa t7.fastq t8.fastq

cat t1.fastq t2.fastq t3.fastq t4.fastq t5.fastq t6.fastq t7.fastq t8.fastq > combine1000wm1e1.fastq
groot align -i ../../groot_index/ -f combine1000werr.fastq > reads1000wm1e1.bam
groot report -i reads1000wm1e1.bam

#	AY6974601_1D    104     885     1D879M5D
#	AY4217611_3A    50      258     258M
#	AY6974601_2B    17      297     296M1D
#	AY4217611_VP3   181     720     5D715M
#	AY4217611_2A    90      450     6D444M
#	AY4217611_VP2   137     765     3D762M
#	AY4217611_3C    149     549     9D534M6D
#	AY6974601_1C    76      732     5D727M
#	AY4217611_2C    207     987     2D961M24D
#	AY4217611_3D    288     1386    1386M
#	AY4217611_VP1   164     882     2D879M1D




###################	 	CONTAMINATION FROM COMMON SOURCES 		#########################
wgsim -R 0 -r 0 -e 0 -N 100000 -1 100 -2 100 ../contamination/KC994741.1.fa t3.fastq t4.fastq
groot align -i ../groot_index/ -f t5.fastq,t6.fastq > CP011305.bam
groot report -i CP011305.bam