-- Zapytanie zwraca imie i nazwisko klientów, którzy zamówili więcej niż jedną rzecz.
SELECT k.imie, k.nazwisko, k.pesel 
FROM klienci k
JOIN zamowienia z ON k.pesel = z.pesel 
WHERE z.ilosc > 1; 

-- Zapytanie zwraca klientów, których imie rozpoczyna się na literę 'M'.
SELECT * FROM klienci 
WHERE imie LIKE 'M%';

-- Zapytanie zwraca najdroższy produkt.
SELECT nazwa_produktu, cena AS Najdroższy_produkt 
FROM produkty 
WHERE cena = (SELECT MAX(cena) FROM produkty);

-- Zamówienia klienta Mateusz Nowak.
SELECT * FROM zamowienia 
WHERE pesel = (SELECT pesel FROM klienci WHERE imie ='Mateusz' AND nazwisko = 'Nowak');

-- Zapytanie wyświetla wszytskie adresy z Katowic posortowane alfabetycznie po ulicach.
SELECT * FROM adresy 
WHERE miasto = 'Katowice' ORDER BY ulica;