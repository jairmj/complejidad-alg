def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        min_pos = i
        for j in range(i+1, n):
            if A[j] < A[min_pos]:
                min_pos = j
        if min_pos != i:
            A[min_pos], A[i] = A[i], A[min_pos] #swap

def bubbleSort(A):
    n = len(A)
    for i in  range(n - 1):
        for j in range(n - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]

def stringMatching(p, t):
    l = len(p)
    n = len(t)
    resultados = []
    for i in range(n - l):
        if p == t[i:i+l]:
            resultados.append(i)
    return resultados


X = [3, 1, 5, 7, 2, 9, 10, 12, 11]
print(stringMatching('rac', 'abracadabracamal'))
bubbleSort(X)
print(X)