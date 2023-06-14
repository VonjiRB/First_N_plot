from collections import defaultdict
from Bio import SeqIO
import gzip
#%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt

file_path = r'C:\Users\Vonji\Desktop\ModernSeqFormat\SRR003265.filt.fastq'
recs = []

with open(file_path, "r") as file:
# recs = SeqIO.parse(gzip.open('SRR003265.filt.fastq'), 'fastq')
   recs = list(SeqIO.parse(file, "fastq"))

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
   
n_cnt = defaultdict(int)
for rec in recs:
   for i, letter in enumerate(rec.seq):
      pos = i + 1
      if letter == 'N':
         n_cnt[pos] += 1

seq_len = max(n_cnt.keys())
positions = range(1, seq_len + 1)
fig, ax = plt.subplots()
ax.plot(positions, [n_cnt[x] for x in positions])
ax.set_xlim(1, seq_len)

plt.show()


   
