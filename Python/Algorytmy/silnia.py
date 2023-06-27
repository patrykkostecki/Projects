#Rekurencyjnie
def silnia(n):
    if n == 0:
        return 1
    else:
        return silnia(n-1) * n

#Iteracyjnie
def silnia_i(n):
    x = 1
    for i in range(1,n+1):
        x = x * i
    return x
print(silnia_i(5))

print(silnia(3))