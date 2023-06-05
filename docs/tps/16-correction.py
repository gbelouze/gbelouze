# 1a
L = [x for x in range(101) if x % 2 == 0 or x % 3 == 0]

# 1b
T = [[x for x in range(k, 101, 10)] for k in range(10)]

# 2
U = [x for _ in range(30) for x in range(2, 4)]

# 3c
V = T[1::2]

# 4a
def prefixe(p, s):
    return p == s[:len(p)]

# 4b
def suffixe(p, s):
    return p == s[len(s)-len(p):]

# 4c
def bord(s):
    for i in range(1, len(s)+1):
        if prefixe(s[i:], s):
            return s[i:]

# 5a
False

# 5b
False

# 5c
True

# 5d
def xor(b1, b2):
    return (b1 or b2) and (not b1 or not b2)

# 5d
def nand(b1, b2):
    return not (b1 and b2)
