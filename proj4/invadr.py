from preproc import *
from reads import *
from output import *
import zipfile

filename = 'practice_W_3_chr_1'

genome = read_genome('ref_' + filename + '.txt')

key_length = 50

genome_index = index_genome(genome, key_length,0)

test = genome_index.keys()[0]

paired_reads = reads('reads_' + filename + '.txt')

candidates = []

for pair in paired_reads:
	split = pair.split(',')
	if (split[0] in genome_index and split[1][::-1] in genome_index):
		continue
	if (split[0][::-1] in genome_index and split[1] in genome_index):
		continue
	if (split[0] in genome_index):
		if (len(genome_index[split[0]]) == 1):
			candidates.append(split[0])
	elif (split[0][::-1] in genome_index):
		if (len(genome_index[split[0][::-1]]) == 1):
			candidates.append(split[0][::-1])
	if (split[1] in genome_index):
		if (len(genome_index[split[1]]) == 1):
			candidates.append(split[1])
	elif (split[1][::-1] in genome_index):
		if (len(genome_index[split[1][::-1]]) == 1):
			candidates.append(split[1][::-1])

candidates_set = set(candidates)

reversed_dict = {}

for each in candidates_set:
	reversed_dict[genome_index[each][0]] = each

sorted_pos = sorted(reversed_dict.keys())

for each in sorted_pos:
	print each, reversed_dict[each]

for i in range(len(sorted_pos)-1): 
	if abs(sorted_pos[i] - sorted_pos[i+1]) < key_length:
		del reversed_dict[sorted_pos[i+1]]

inv = []

for each in reversed_dict:
	s = str(reversed_dict[each]) + ',' + str(each)
	inv.append(s)

generate_file(header='>'+filename,INV=inv)

title = 'invadr_key' + str(key_length) + '_' + filename + '.zip'

with zipfile.ZipFile(title,'w') as myzip:
	myzip.write('answer.txt')