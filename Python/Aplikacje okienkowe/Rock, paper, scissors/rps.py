import tkinter
import random

root = tkinter.Tk()
root.title('Kamien, papier, nożyce')
root.geometry('400x400')

text = tkinter.Label(root, text='Kamień, papier, nożyce').pack()


list = ['rock', 'paper', 'scissors']

def play(player, cpu):
    win_with = {'paper':'rock', 'rock':'scissors', 'scissors':'paper'}
    if player == cpu:
        return None
    elif win_with[player] == cpu:
        return True
    else:
        return False

def gra_cmd(player):
    global text
    cpu = random.choice(list)
    is_user_winner = play(player,cpu)
    if is_user_winner is None:
        text.config('Remis!')
    elif is_user_winner is True:
        text.config('Wygrałeś!', fg='green')
    else:
        text.config('Przgrałeś!', fg='red')

tkinter.Button(
    root, text='Kamien', command=lambda: gra_cmd("paper")
).pack()

tkinter.Button(
    root, text='Papier', command=lambda: gra_cmd("rock")
).pack()

tkinter.Button(
    root, text='Nożyce', command=lambda: gra_cmd("scissors")
).pack()

root.mainloop()