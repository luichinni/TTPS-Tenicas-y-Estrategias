from sys import stdin

def RSQ(rsq, seq: list):
    for I in range(1,len(seq)):
        rsq.append(rsq[I-1]+1 if seq[I] == seq[I-1] else rsq[I-1])

try:
    while True:
        ste = [1 if x == '.' else 0 for x in stdin.readline().rstrip()]

        rsq = [0]
        RSQ(rsq,ste)
        casos = int(stdin.readline())

        for J in range(casos):
            L, R = list(map(int,stdin.readline().split()))
            print(rsq[R-1]-rsq[L-1])

except:
    pass
