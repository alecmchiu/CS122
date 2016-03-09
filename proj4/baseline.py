from preproc import *
from reads import *
from output import *
import zipfile

file_sets = ['practice_W_3_chr_1','practice_E_1_chr_1','hw2undergrad_E_2_chr_1']

filename = file_sets[0]

genome = read_genome('ref_' + filename + '.txt')

key_length = 50

fragments = 50/key_length

read_length = 50

genome_index = index_genome(genome, read_length, fragments-1)

test = genome_index.keys()[0]

paired_reads = reads('reads_' + filename + '.txt')
'''
for pair in paired_reads:
	split = pair.split(',')
	kmers1 = kmer_read(split[0],key_length)
	kmers1_rev = kmer_read(split[0][::-1],key_length)
	kmers2 = kmer_read(split[1],key_length)
	kmers2_rev = kmer_read(split[1][::-1],key_length)
	count1 = 0
	count1_rev = 0
	count2 = 0
	count2_rev = 0
	for each in kmers1:
		if (each in genome_index):
			count1 += 1
	for each in kmers2:
		if (each in genome_index):
			count2 += 1
	for each in kmers1_rev:
		if (each in genome_index):
			count1_rev += 1
	for each in kmers2_rev:
		if (each in genome_index):
			count2_rev += 1
	if (count1 > fragments and count2_rev > fragments):
		continue
	if (count1_rev > fragments and count2 > fragments):
		continue
	total = set(kmers1 + kmers2 + kmers1_rev + kmers2_rev)
	for each in total[:]:
		if each not in genome_index:
			total.remove(each)
		else:
			if (len(genome_index[each]) > fragments):
				total.remove(each)
'''

candidates = []

for pair in paired_reads:
	split = pair.split(',')
	if (split[0] in genome_index and split[1][::-1] in genome_index):
		continue
	if (split[0][::-1] in genome_index and split[1] in genome_index):
		continue
	if (split[0] in genome_index and split[1] in genome_index):
		print "yes"
	if (split[0][::-1] in genome_index and split[1][::-1] in genome_index):
		print "yes"
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

#for each in sorted_pos:
#	print each, reversed_dict[each]

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