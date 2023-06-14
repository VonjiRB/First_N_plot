from Bio import SeqIO    # 48/306
import gzip
#from collections import defaultdict


file_path = r'C:\Users\Vonji\Desktop\ModernSeqFormat\SRR003265.filt.fastq'  # Provide the correct file path here

# Open the gzip-compressed file using Biopython's SeqIO module
with open(file_path, "r") as file:
    records = SeqIO.parse(file, "fastq")

    # Iterate over the records in the file and keep track of the count
    count = 0
    for record in records:
        # Print the record's ID, description, sequence, and letter annotations
        print("ID:", record.id)
        print("Description:", record.description)
        print("Sequence:", record.seq)
        print("Letter annotations:", record.letter_annotations)
        print("---")
        
        # Increment the count
        count += 1
        
        # Exit the loop after printing the first 20 records
        if count == 20:
            break

#recs = SeqIO.parse(gzip.open('SRR003265.filt.fastq'), 'fastq') 
#recs = SeqIO.parse(file, 'fastq')
#cnt = defaultdict(int)

#for rec in records:
   #for letter in rec.seq:
      #cnt[letter] += 1
#tot = sum(cnt.values())
#for letter, cnt_value in cnt.items():
    #print('%s: %.2f %d' % (letter, 100. * cnt.value / tot, cnt_value))