def horner(x, tab):
    result = tab[0]
    for i in range(1, len(tab)):
        result = result * x + tab[i]
    return result

print(horner(3, [1,-3,5,15])) #reszta z dzielenia

def horner_r(x,tab):
    if len(tab) == 1:
        return
    return horner_r(x, tab[1:]) * x + tab[0]

print(horner_r(3, [1,-3,5,15]))