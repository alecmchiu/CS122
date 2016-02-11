#Edit Distance Alignment

from math import ceil

def NW(s1,s2):
	a = '$' + s1
	b = '$' + s2
	F = []
	for i in range(len(a)):
		F.append([0]*(len(b)))
	for i in range(1,len(a)):
		F[i][0] = i
	for j in range(1,len(b)):
		F[0][j] = j
	for i in range(1,len(a)):
		for j in range(1,len(b)):
			match = F[i-1][j-1] + (0 if a[i]==b[j] else 1)
			delete = F[i-1][j] + 1
			insert = F[i][j-1] + 1
			F[i][j] = min(delete, match, insert)

	dist = F[len(a)-1][len(b)-1]
	alignment_a = ''
	alignment_b = ''
	i = len(a) - 1
	j = len(b) - 1

	while i > 0 or j > 0:
		if i > 0 and (F[i][j] == (F[i][j-1] + 1)):
			alignment_a = '-' + alignment_a
			alignment_b = b[j] + alignment_b
			j -= 1
		elif i > 0 and j > 0 and F[i][j] == (F[i-1][j-1] + (0 if a[i] == b[j] else 1)):
			alignment_a = a[i] + alignment_a
			alignment_b = b[j] + alignment_b
			i -= 1
			j -= 1
		else:
			alignment_a = a[i] + alignment_a
			alignment_b = '-' + alignment_b
			i -= 1

	return dist, alignment_a, alignment_b

def EditDistance(s,t):
	'''Returns edit distance between s and t '''

	# #base cases
	# if (s == t):
	# 	return [0]
	# if (len(s) == 0):
	# 	return [len(t)]
	# if (len(t) == 0):
	# 	return [len(s)]

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

	return vec1 #return bottom row

def PartionY(left,right):
	total = [sum(x) for x in zip(left,right)]
	index = 0
	min = total[0]
	for i in range(len(total)):
		if total[i] < min:
			index = i
			min = total[i]
	return index

def Hirschberg(x,y):
	z = ''
	w = ''

	if len(x) == 0:
		for i in range(len(y)):
			z = '-' * len(y)
			w = y
	elif len(y) == 0:
		for i in range(len(x)):
			z = x
			w = '-' * len(x)
	elif (len(x) == 1 or len(y) == 1):
		z,w = NW(x,y)
	else:
		xmid = int(ceil(len(x)/2.0))

		ScoreL = EditDistance(x[:xmid],y)
		ScoreR = EditDistance(x[xmid::-1],y[::-1])
		ymid = PartionY(ScoreL, ScoreR)

		zl,wl = Hirschberg(x[:xmid],y[:ymid])
		zr,wr = Hirschberg(x[xmid:],y[ymid:])
		z,w = zl+zr,wl+wr

	return z,w


input = open('rosalind_edta.txt','r')
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

s = NW(s1,s2)
output = open('editalignment.txt','w')
output.write(str(s[0]) + '\n')
output.write(s[1] + '\n')
output.write(s[2] + '\n')

"""
s = NW('PRETTY','PRTTEIN')
print s[0]
print s[1]
print s[2]
"""
#s = Hirschberg('PRETTY','PRTTEIN')
#s = Hirschberg('AGTACGCA','TATGC')