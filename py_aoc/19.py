from util import get_data

def parsefunc(s):
    return s.strip()

def main(seq):
    a, b = int(seq[22].split()[2]), int(seq[24].split()[2])
    n1 = 836 + 22 * a + b
    n2 = n1 + 10550400
    for n in (n1, n2):
        sqn = int(n ** .5)
        yield sum(d + n // d for d in range(1, sqn + 1) if n % d == 0) - sqn * (sqn ** 2 == n)

seq = get_data(19, parsefunc)
result = [n for n in main(seq)]

print("P1: ", result[0])
print("P2: ", result[1])
