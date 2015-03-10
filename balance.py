def is_balanced(s):
    d = 0   # depth
    i = 0   # index
    for c in s:
        if c == '(':
            d += 1
        elif c == ')':
            if d > 0:
                d -= 1
            else:
                return "umatched ')' at index " + str(i)
        i += 1
    if d == 0:
        return "balanced"
    else:
        return "unmatched '('"

if __name__ == '__main__':
    import sys
    for arg in sys.argv[1:]:
        print("{:20} {}".format(arg + ':', is_balanced(arg)))
