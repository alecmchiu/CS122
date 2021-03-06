from itertools import permutations

def pick_maximal_overlap(reads, k):
    reada, readb = None, None
    best_olen = 0
    for a, b in permutations(reads, 2):
        olen = overlap(a, b, k)
        if olen > best_olen:
            reada, readb = a, b
            best_olen = olen
    return reada, readb, best_olen

def greedy_scs(reads, k):
    read_a, read_b, olen = pick_maximal_overlap(reads, k)
    while olen > 0:
        reads.remove(read_a)
        reads.remove(read_b)
        reads.append(read_a + read_b[olen:])
        read_a, read_b, olen = pick_maximal_overlap(reads, k)
    return ''.join(reads)

def overlap(x, y, k):
    idx = len(y)
    while True:
        hit = y.rfind(x[-k:], 0, idx)
        if hit == -1:
            return 0
        ln = hit + k
        if x[-ln:] == y[:ln]:
            return ln
        idx = hit + k - 1
    return -1

#ls = ['ATTAC','TACAG','GATTA','ACAGA','CAGAT','TTACA','AGATT']
ls = []
input = open('rosalind_pcov.txt','r')
for line in input:
    ls.append(line.strip())
input.close()
s = len(ls)

output = open('cyclicchromosome.txt','w')
output.write(greedy_scs(ls,1)[:s])
output.close()