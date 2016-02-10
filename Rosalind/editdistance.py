#LevenshteinDistance
#Iterative Approach using Two Rows

"""
This approach goes row by row and uses two rows by continually overriding
each row until the bottom row is reached and the bottom right corner of
the edit distance matrix can be retrieved.
"""

def EditDistance(s,t):
	'''Returns edit distance between s and t '''

	#base cases
	if (s == t):
		return 0
	if (len(s) == 0):
		return len(t)
	if (len(t) == 0):
		return len(s)

	#create two rows
	#both rows should be length of t+1
	vec0 = []
	vec1 = [None] * (len(t)+1) #initialized for index editing purposes

	for i in range(len(t)+1):
		vec0.append(i) #initialize first row of matrix

	for i in range(len(s)):
		vec1[0] = i+1 #initialize second row
		for j in range(len(t)):
			if (s[i] == t[j]):
				cost = 0 #match
			else:
				cost = 1 #assuming all operations cost 1
			vec1[j+1] = min(vec1[j]+1,vec0[j+1]+1,vec0[j]+cost) #choose cheapest operation
		for j in range(len(t)+1):
			vec0[j] = vec1[j] #copy next row

	return vec1[len(t)] #return bottom right corner

input = open('rosalind_edit.txt','r')
s1 = ''
s2 = ''
input.next()
for line in input:
	if (line.strip()[0] == '>'):
		break
	else:
		s1 = s1 + line.strip()
for line in input:
	s2 = s2 + line.strip()
input.close()

print EditDistance(s1,s2)