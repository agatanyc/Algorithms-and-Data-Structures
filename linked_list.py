# Quadratic -- i.e., O(n * n)
# def create_list(values):
#    return (values[0], create_list(values[1:])) if values else None

# Linear -- i.e., O(n)

def create_list(values, i=0):
    return (values[i], create_list(values, i + 1)) if i < len(values) else None

def head(xs):
    return xs[0]

def tail(xs):
    """Returns the tail of xs - the second element of the tuple."""
    return xs[1]

def cons(x, xs):
    return (x, xs)

def push(xs, x):
    return (x, xs)

def pop(xs):
    """Returns two values: The first element of xs, and the tail of xs."""
    return xs

def append(xs, x):
    return (xs[0], append(xs[1], x)) if xs else (x, None)

enqueue = append
dequeue = pop

w = 40  # Width of the first column of output.
xs = create_list((1, 2, 3))
print("{:40} {}".format("xs = create_list(1, 2, 3)"     , xs                ))
print("{:40} {}".format("head(xs)"                      , head(xs)          ))
print("{:40} {}".format("tail(xs)"                      , tail(xs)          ))
print("{:40} {}".format("cons('a', xs)"                 , cons('a', xs)     ))
print("{:40} {}".format("push(xs, 'a')"                 , push(xs, 'a')     ))

y, ys = pop(xs)
print("{:40} {}, {}".format("y, ys = pop(xs)", y, ys))
