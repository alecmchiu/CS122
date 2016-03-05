from preproc import *
from reads import *
from output import *
import zipfile

filename = 'practice_E_1_chr_1'

genome = read_genome('ref_' + filename + '.txt')

key_length = 50

genome_index = index_genome(genome, key_length,0)

test = genome_index.keys()[0]

paired_reads = reads('reads_' + filename + '.txt')

half_reads = []

for pair in paired_reads:
	half_reads.append(pair.split(',')[0])

candidates = []

for read in half_reads:
	if read in genome_index and read[::-1] in genome_index:
		continue
	if read not in genome_index and read[::-1] in genome_index:
		candidates.append(read[::-1])

candidates_set = set(candidates)

reversed_dict = {}

for each in candidates_set:
	reversed_dict[genome_index[each][0]] = each

sorted_pos = sorted(reversed_dict.keys())

for i in range(len(sorted_pos)-1): 
	if abs(sorted_pos[i] - sorted_pos[i+1]) < key_length:
		del reversed_dict[sorted_pos[i+1]]

inv = []

for each in reversed_dict:
	s = str(reversed_dict[each]) + ',' + str(each)
	inv.append(s)

generate_file(header='>'+filename,INV=inv)

title = 'invadr_half_read_' + filename + '.zip'

with zipfile.ZipFile(title,'w') as myzip:
	myzip.write('answer.txt')