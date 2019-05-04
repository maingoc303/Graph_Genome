from Bio import SeqIO
import os


gbk_filename = os.listdir('gb_files')

#faa_filename = "NC_005213_converted.fna"

for gb_f in gbk_filename:
	input_handle  = open('gb_files/'+gb_f, "r")
	fa_f = 'fa_files/'+gb_f.replace('.gb','.fa')
	output_handle = open(fa_f, "w")
	# convert file by file from gb to fa
	for seq_record in SeqIO.parse(input_handle, "genbank") :
	    #print "Dealing with GenBank record %s" % seq_record.id
	    output_handle.write(">%s %s\n%s\n" % (
	           seq_record.id,
	           seq_record.description,
	           seq_record.seq))
	output_handle.close()
	input_handle.close()