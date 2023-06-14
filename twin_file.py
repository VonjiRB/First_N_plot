from Bio import SeqIO    # 48/306
import gzip

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