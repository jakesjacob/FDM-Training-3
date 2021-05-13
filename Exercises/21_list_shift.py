

listt = [20, 45, 2, 1, 55, 14]


def shift(seq, n=0):
    a = n % len(seq)
    return seq[+a:] + seq[:+a]


print(listt)
listt = shift(listt, 1)
print(listt)
