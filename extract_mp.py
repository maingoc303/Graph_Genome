from Bio import SeqIO
import os

accession_no = []

filepath = 'ID.txt' # file that contain list of accession numbers
with open(filepath) as fp:
   line = fp.readline()
   n = 1
   while line:
       accession_no.append(line.strip())
       line = fp.readline()
       n += 1

  ### obtain the dictionary for checking number of protein of each accession_no
  access_vs_no_prot = dict()


### extract all fna files to folder fna_out
os.mkdir('fna_out')
for id in accession_no:
  # extract fna files
    genbank_file = os.getcwd() + '/gb_files/'+id+'.gb'
    records = SeqIO.read(open(genbank_file, "r"), "genbank")
    sequence = records.seq
    features = records.features
    start = [features[i].location.nofuzzy_start for i in range(1, len(features)) if features[i].type == "mat_peptide"]
    end = [features[i].location.nofuzzy_end for i in range(1, len(features)) if features[i].type == "mat_peptide"]
    pep_seq = [features[i].extract(sequence) for i in range(1, len(features)) if features[i].type == "mat_peptide"]
    protein_name = [features[i].qualifiers.get("product")[0] for i in range(2,len(features)) if features[i].type == "mat_peptide"]
    msa_file = os.getcwd() + '/fna_out/' + id + '.fna'
    with open(msa_file, 'w') as msa:
        for i in range(len(start)):
            msa.write('>%s_%s %i_%i\n%s\n' % (id, protein_name[i], start[i], end[i], pep_seq[i]))
  # dictionary for number of protein per accession_no
    access_vs_no_prot[id] = len(protein_name)


# combine all fna files to one and save under fna format
file_names = os.listdir('fna_out/')
output = ''
for file in file_names:
    with open(os.getcwd()+'/fna_out/'+file) as f:
        content = f.read().strip('\n')
    output += content + '\n'  #  This will use a placeholder of 0 for all labels.
    
with open('combine.fna', 'wb') as f:
    f.write(output)


