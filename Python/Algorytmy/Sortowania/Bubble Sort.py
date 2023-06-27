#Sorotwanie bąbelkowe
#Bubble sort

tab = [8, 2, 1, 9, 4, 3]
print(tab)

i = 0

while i < len(tab) -1:
    j = 0
    while j < len(tab) -1:
        if tab[j] > tab[j + 1]:
            tab[j], tab[j+1] = tab[j+1], tab[j]
        j+=1
    i +=1
    print(tab)
