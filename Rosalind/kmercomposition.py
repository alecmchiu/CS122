from itertools import product

k = 4

kmers = { ''.join(key): 0 for key in product('ATCG',repeat=k)}

input = open('rosalind_kmer.txt','r')
input.next()
string = ''
for line in input:
	string = string + line.strip()
input.close()

for i in range(len(string)-k+1):
	kmers[string[i:i+k]] += 1

output = open('kmercomposition.txt','w')
for each in sorted(kmers.keys()):
	output.write(str(kmers[each]) + ' ')

output.close()

