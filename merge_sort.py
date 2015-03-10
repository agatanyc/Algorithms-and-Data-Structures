def merge_sort(xs):
    if len(xs) <= 1:
        return xs

    mid = len(xs) // 2
    left = xs[:mid]
    right = xs[mid:]

    merge_sort(left)
    merge_sort(right)

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            xs[k] = left[i]
            i += 1
        else:
            xs[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        xs[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        xs[k] = right[j]
        j += 1
        k += 1

    return xs

xs = [1, 5, 3, 2, 6, 9, 4]
print(merge_sort(xs))
