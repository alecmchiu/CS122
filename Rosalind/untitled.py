from itertools import permutations
from collections import defaultdict

reads = []
input = open('LeahInput.txt','r')
input.next()
current = ''
for line in input:
	stripped = line.strip()
	if stripped[0] == '>':
		reads.append(current)
		current = ''
	else:
		current = current + stripped
reads.append(current)
input.close()

def overlap(a, b):
	min_length = 500
	start = 0
	while True:
		start = a.find(b[:min_length], start)
		if start == -1:
			return 0
		if b.startswith(a[start:]):
			return len(a)-start
		start += 1

# def overlap2(s1,s2):
# 	k = min(len(s1)/2,len(s2)/2)
# 	if len(s1) < k or len(s2) < k:
# 		return 0
# 	index = len(s2)
# 	while True:
# 		hit = s2.rfind(s1[-k:],0,index)
# 		if hit == -1:
# 			return 0
# 		extension = hit + k
# 		if s1[-extension:] == s2[:extension]:
# 			return extension
# 		index = hit + k - 1

# overlap_matrix = defaultdict(dict)

# def compute_matrix(reads):
# 	for each in permutations(reads,2):
# 		s1 = each[0]
# 		s2 = each[1]
# 		pair_overlap = overlap(s1,s2)
# 		overlap_matrix[s1][s2] = pair_overlap

# def max_overlap(reads):
# 	read1 = ''
# 	read2 = ''
# 	best_overlap = 0
# 	for each in permutations(reads,2):
# 		s1 = each[0]
# 		s2 = each[1]
# 		pair_overlap = overlap_matrix[s1][s2]
# 		if pair_overlap > best_overlap:
# 			best_overlap = pair_overlap
# 			read1 = s1
# 			read2 = s2
# 	return read1, read2, best_overlap

# def scs(reads):
# 	if len(reads) == 1:
# 		return reads[0]
# 	compute_matrix(reads)
# 	read1, read2, best_overlap = max_overlap(reads)
# 	new_reads = []
# 	while len(reads) > 0:
# 		new_string = read1 + read2[best_overlap:]
# 		reads.remove(read1)
# 		reads.remove(read2)
# 		new_reads.append(new_string)
# 		read1, read2, best_overlap = max_overlap(reads)
# 	return scs(new_reads)

def max_overlap(reads):
	read1 = ''
	read2 = ''
	best_overlap = 0
	for each in permutations(reads,2):
		s1 = each[0]
		s2 = each[1]
		pair_overlap = overlap(s1,s2)
		if pair_overlap > best_overlap:
			best_overlap = pair_overlap
			read1 = s1
			read2 = s2
	return read1, read2, best_overlap

def scs(reads):
	new_string = ''
	read1, read2, best_overlap = max_overlap(reads)
	while best_overlap > 0:
		new_string = read1 + read2[best_overlap:]
		reads.remove(read1)
		reads.remove(read2)
		reads.append(new_string)
		read1, read2, best_overlap = max_overlap(reads)
	return ''.join(reads)

output = open('output.txt','w')
output.write(scs(reads))
output.close()