
def addr(R, a, b, c):
    result = [R[0], R[1], R[2], R[3]]
    result[c] = result[a] + result[b]
    return result

def addi(R, a, b, c):
    result = [R[0], R[1], R[2], R[3]]
    result[c] = result[a] + b
    return result

def mulr(R, a, b, c):
    result = [R[0], R[1], R[2], R[3]]
    result[c] = result[a] * result[b]
    return result

def muli(R, a, b, c):
    result = [R[0], R[1], R[2], R[3]]
    result[c] = result[a] * b
    return result

def banr(R, a, b, c):
    result = [R[0], R[1], R[2], R[3]]
    result[c] = result[a] & result[b]
    return result

def bani(R, a, b, c):
    result = [R[0], R[1], R[2], R[3]]
    result[c] = result[a] & b
    return result

def borr(R, a, b, c):
    result = [R[0], R[1], R[2], R[3]]
    result[c] = result[a] | result[b]
    return result

def bori(R, a, b, c):
    result = [R[0], R[1], R[2], R[3]]
    result[c] = result[a] | b
    return result

def setr(R, a, b, c):
    result = [R[0], R[1], R[2], R[3]]
    result[c] = result[a]
    return result

def seti(R, a, b, c):
    result = [R[0], R[1], R[2], R[3]]
    result[c] = a
    return result

def gtir(R, a, b, c):
    result = [R[0], R[1], R[2], R[3]]
    result[c] = bool(a > result[b])
    return result

def gtri(R, a, b, c):
    result = [R[0], R[1], R[2], R[3]]
    result[c] = bool(result[a] > b)
    return result

def gtrr(R, a, b, c):
    result = [R[0], R[1], R[2], R[3]]
    result[c] = bool(result[a] > result[b])
    return result

def eqir(R, a, b, c):
    result = [R[0], R[1], R[2], R[3]]
    result[c] = bool(a == result[b])
    return result

def eqri(R, a, b, c):
    result = [R[0], R[1], R[2], R[3]]
    result[c] = bool(result[a] == b)
    return result

def eqrr(R, a, b, c):
    result = [R[0], R[1], R[2], R[3]]
    result[c] = bool(result[a] == result[b])
    return result
