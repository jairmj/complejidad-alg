#Se sobreentiende que tenemos los coeficientes

a = [10, 20, 0, 1, 23, 4]

def p(x, coefs):
    sum = 0.0
    #coefs.reverse()
    #n=len(a)
    for i, ai in enumerate(reversed(coefs)):
        sum += ai * x **i
        #n-=1
    return sum
print(p(2,a))