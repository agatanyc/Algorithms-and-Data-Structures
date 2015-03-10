def reverse_stack(xs):
    s = []
    for x in list(xs):
        p = xs.pop()
        s.append(p)
    return s

xs = [1, 2, 3]
print(reverse_stack(xs))
