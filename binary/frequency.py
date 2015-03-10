def freq_1(xs, t):
    for i, x in enumerate(xs[:len(xs)//2]):
        if x == t:
            return i

def freq_2(xs, t):
    for i, x in enumerate(xs[len(xs)//2:]):
        if x == t:
            return i + 1

def freq(xs, x):
    lo = freq_1(xs, x)
    hi = freq_2(xs, x)
    return hi - lo if lo else hi + 1

xs = [ 1, 2, 3, 3, 5, 5, 6]
t = 5

print(freq(xs, 5))
