def Wezel():
    def __init__(self, dane = None):
        self.dane = dane
        self.lewe_dziecko = None
        self.prawe_dziecko = None

class BST():
    def __init__(self):
        self.korzen = Wezel()

    def dodaj(self, dane):
        if self.korzen.dane == None:
            self.korzen.dane =dane
        else:
            def dodaj_do_wierzcholka(dane, wierzcholek):
                if dane < wierzcholek.dane:
                    if wierzcholek.lewe_dziecko == None:
                        wierzcholek.lewe_dziecko = Wezel(dane)
                    else:
                        dodaj_do_wierzcholka(dane, wierzcholek.lewe_dziecko)
                if dane > wierzcholek.dane:
                    if wierzcholek.prawe_dziecko == None:
                        wierzcholek.prawe_dziecko  = Wezel(dane)
                    else: dodaj_do_wierzcholka(dane, wierzcholek.prawe_dziecko)

            dodaj_do_wierzcholka(dane, self.korzen)

        def wyswietl(self):
