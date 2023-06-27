# Sortowanie przez scalanie
# Merge sort

tab = [8, 2, 1, 9, 4, 3]
print(tab)


def mergeSort(tab):
    if len(tab) > 1:
        mid = len(tab) // 2
        L = tab[:mid]
        P = tab[mid:]
        mergeSort(L)
        mergeSort(P)

        i = j = k = 0

        while i < len(L) and j < len(P):
            if L[i] < P[j]:
                tab[k] = L[i]
                i += 1
            else:
                tab[k] = P[j]
                j += 1
            k += 1

        while i < len(L):
            tab[k] = L[i]
            i += 1
            k += 1

        while j < len(P):
            tab[k] = P[j]
            j += 1
            k += 1


mergeSort(tab)
print("Posortowana: ", tab)