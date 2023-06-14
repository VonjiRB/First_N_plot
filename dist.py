from collections import defaultdict
from Bio import SeqIO
import gzip

file_path = r'C:\Users\Vonji\Desktop\ModernSeqFormat\SRR003265.filt.fastq'
with open(file_path, "r") as file:
# recs = SeqIO.parse(gzip.open('SRR003265.filt.fastq'), 'fastq')
   recs = SeqIO.parse(file, "fastq")
   cnt = defaultdict(int)
   counter = 0

   for rec in recs:
      for letter in rec.seq:
         cnt[letter] += 1
      counter += 1
         
      tot = sum(cnt.values())
      for letter, cnt_value in cnt.items():
         print('%s: %.2f %d' % (letter, 100. * cnt_value / tot, cnt_value))

      if counter >= 200:
         break


   
