from preproc import read_genome, index_genome, parse_consensus
from output import generate_file
import zipfile
import re
from time import clock

script_start = clock()

file_sets = ['practice_W_3_chr_1','practice_E_1_chr_1','hw2undergrad_E_2_chr_1']

filename = file_sets[2]

key_length = 20

genome = read_genome('ref_' + filename + '.txt')
genome_index = index_genome(genome, key_length, 0)

consensus = parse_consensus('consensus_' + filename + '.txt')
consensus_rev = consensus[::-1]

STR_regex = r'(\w\w\w+)\1{2,7}'

candidates = set()

for i in range(len(consensus_rev)-key_length):
	fragment = consensus_rev[i:i+key_length]
	if (fragment in genome_index):
		if(re.search(STR_regex,fragment) == None):
			candidates.add(fragment)

pos = []

for each in candidates:
	pos.append(genome_index[each][0])

pos.sort()

final_pos = []
inv = []

i = 0
start = pos[i]
end = pos[i] + key_length
while i < len(pos):
	if i == len(pos) - 1:
		inv.append(genome[pos[i]:pos[i]+key_length] + ',' + str(pos[i]))
		break
	if (pos[i+1] - pos[i] < key_length):
		end = pos[i+1] + key_length
		i += 1
	elif pos[i+1] - pos[i] > key_length:
		inv.append(genome[start:end] + ',' + str(start))
		start = pos[i+1]
		end = start + key_length
		i += 1

for each in inv:
	print each

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

script_end = clock()

print "Execution time: {0:.3f}s".format(script_end-script_start)