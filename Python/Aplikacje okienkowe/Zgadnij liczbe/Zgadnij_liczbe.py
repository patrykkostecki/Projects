import random
import tkinter as tk

root = tk.Tk()
root.geometry('300x300')
tekst = tk.Label(root, text='Zgadnij liczbę!').pack()

g = tk.Entry(root)
g.pack()

x = random.choice(range(0,10))

guess = None

i = 0

def zg(guess):
    wynik = tk.Label(root, text='')
    wynik.pack()
    i = 0

    guess_str = g.get()
    guess = int(guess_str)

    if guess == x:
        wynik.config(text=f'Zgadłeś! Liczba to {x}')
        zgadnij.config(state='disabled')
    elif guess < x:
        wynik.config(text='Liczba jest za mała!')
    elif guess > x:
        wynik.config(text='Liczba jest za duża')


zgadnij = tk.Button(root, text='Zgadnij!', command=lambda: zg(guess))
zgadnij.pack()






root.mainloop()
