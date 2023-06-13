#  FASTQ file
# @SRR003258.1 30443AAXX:1:1:1053:1999 length=51 
#ACCCCCCCCCACCCCCCCCCCCCCCCCCCCCCCCCCCACACACACCAACAC 
#+ 
#=IIIIIIIII5IIIIIII>IIII+GIIIIIIIIIIIIII(IIIII01&III # somehow score ???

from Bio import SeqIO
from Bio import Data
import gzip
import Bio

file_path = r'C:\Users\Vonji\Desktop\ModernSeqFormat\SRR003265.filt.fastq' # Provide the correct file path here
# Open the file using Biopython's SeqIO module
with open(file_path, "r") as file:
    records = SeqIO.parse(file, "fastq")

    # Iterate over the records in the file
    for record in records:
        # Process each record as needed
        print(record)

recs = SeqIO.parse(gzip.open('SRR003265.filt.fastq.gz'), 'fastq') # 1 jusqu'à 2032904
rec = next(recs)

print(rec.id, rec.description, rec.seq)
print(rec.letter_annotations)









