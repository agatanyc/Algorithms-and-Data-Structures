import bisect

def count(xs, x):
    lo = bisect.bisect_left(xs, x)
    hi = bisect.bisect_right(xs, x)
    return hi - lo

xs = [1, 2, 3, 4, 5, 5, 5, 7, 8]
x = 5

print(count(xs, 5))
