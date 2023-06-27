tekst = open('tekst.txt', 'r')
txt = tekst.read()
tekst.close()

def slowa(txtt):
    ilosc = {}
    words = txtt.split()
    for word in words:
        if word in ilosc:
            ilosc[word] += 1
        else:
            ilosc[word] = 1

    return ilosc
print(slowa(txt))

def litery(txttt):
    a = 'abcdefghijkmnloupr stwz'
    b = {}
    for i in txttt:
        if i.lower() in a:
            if i.lower() in b:
                b[i.lower()] += 1
            else:
                b[i.lower()] = 1
    return b

print(litery(txt))

def bubbleSort():
    pass

def insertionSort():
    pass