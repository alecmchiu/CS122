from preproc import read_genome, index_genome, parse_consensus
from output import generate_file
import zipfile
import re

file_sets = ['practice_W_3_chr_1','practice_E_1_chr_1','hw2undergrad_E_2_chr_1']

filename = file_sets[2]

key_length = 50

genome = read_genome('ref_' + filename + '.txt')
genome_index = index_genome(genome, key_length, 0)

consensus = parse_consensus('consensus_' + filename + '.txt')
consensus_rev = consensus[::-1]

STR_regex = r'(\w\w+)\1{7,25}'

candidates = set()

for i in range(len(consensus_rev)-key_length):
	fragment = consensus_rev[i:i+key_length]
	if (fragment in genome_index):
		if (len(genome_index[fragment]) == 1):
			if(re.search(STR_regex,fragment) == None):
				candidates.add(fragment)

for each in candidates:
	print each,genome_index[each]

inv = []

for each in candidates:
	s = str(each) + ',' + str(genome_index[each][0])
	inv.append(s)

if filename != file_sets[2]:
	generate_file(header='>'+filename,INV=inv)
else:
	f = open('good_answer.txt','r')
	answer = open('answer.txt','w')
	for line in f:
		answer.write(line)
	answer.write('>INV\n')
	for item in inv:
		answer.write("{}\n".format(item))
	f.close()
	answer.close()

title = 'invadr_key' + str(key_length) + '_' + filename + '.zip'

with zipfile.ZipFile(title,'w') as myzip:
	myzip.write('answer.txt')