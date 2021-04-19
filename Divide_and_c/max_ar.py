def max(a, i, j):
    if i == j:
        return a[i]

    med = (i+j)//2
    maxI = max(a, i, med)
    maxD = max(a, med +1 , j)
    if maxI > maxD:
        return maxI
    else:
        return maxD

a = [23, 42, 12, 4, 9, 13, 53, 23, 1]

print(max(a, 0, len(a) - 1))