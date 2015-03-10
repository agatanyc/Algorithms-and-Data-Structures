def choose_pivot(lo, hi):
    return lo + (hi - lo + 1) // 2

def partition_array(xs, lo, hi):
    p = choose_pivot(lo, hi)
    xs[p], xs[hi] = xs[hi], xs[p]
    e = lo
    for i in range(lo, hi):
        if xs[i] < xs[hi]:
            xs[e], xs[i] = xs[i], xs[e]
            e += 1
    xs[e], xs[hi] = xs[hi], xs[e]
    return e    # final location of the pivot value

def sort(xs):
    def imp(lo, hi):
        if lo < hi:
            p = partition_array(xs, lo, hi)
            imp(lo, p - 1)
            imp(p + 1, hi)
    imp(0, len(xs) - 1)

if __name__ == '__main__':
    #xs = [2, 7, 3, 8, 11, 5, 9, 17]
    #sort(xs)
    #print(xs)

    import random
    xs = [0, 3, 5, 6, 7, 8, 9]
    random.shuffle(xs)
    print(xs)
    sort(xs)
    print(xs)
