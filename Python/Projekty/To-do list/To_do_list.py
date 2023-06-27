class to_do_list():
    def __init__(self):
        self.Stack = []
        self.load_data()  # załaduj dane z pliku przy uruchomieniu programu

    def dodaj(self, s):
        self.Stack.append(s)
        self.save_data()  # zapisz dane po dodaniu nowego elementu

    def zadania(self):
        self.is_empty()
        for i in range(len(self.Stack)):
            print(self.Stack[i])

    def usun(self):
        self.is_empty()
        x = int(input('Które zadanie chcesz usunąć? '))
        self.Stack.pop(x-1)
        self.save_data()  # zapisz dane po usunięciu elementu

    def edytuj(self):
        self.is_empty()
        x = int(input('Które zadanie chcesz edytować?'))
        new = input('Wpisz nową treść zadania')
        self.Stack[x-1], new = new, self.Stack[x-1]
        self.save_data()  # zapisz dane po edycji elementu

    def load_data(self):
        try:
            with open('data.txt', 'r') as f:
                self.Stack = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            pass

    def save_data(self):
        with open('data.txt', 'w') as f:
            for item in self.Stack:
                f.write(item + '\n')

    def is_empty(self):
        if len(self.Stack) <= 0:
            print("Twoja lista zadań jest pusta!")

cj = to_do_list()

user_name = input('Cześć! Jak się nazywasz? ')
print(f'Witaj {user_name}')

while True:
    print('Jeśli chcesz zobaczyć listę swoich zadań wpisz 1')
    print('Jeśli chcesz dodać jakies zadanie wpisz 2')
    print('Jeśli chcesz edytować jakies zadanie wpisz 3')
    print('Jeśli chcesz usunąć jakies zadanie wpisz 4')
    print('Jeśli chcesz zakończyć wpisz 5')

    x = int(input('Co chciałbyś dzisiaj zrobić? '))

    if x == 1:
        cj.zadania()
    elif x == 2:
        while True:
            task_name = input('Wpisz swoje zadanie(Wpisz stop aby przerwać): ')
            if task_name == 'stop':
                break
            else:
                cj.dodaj(task_name)
    elif x == 3:
        cj.edytuj()
    elif x == 4:
        cj.usun()
    elif x == 5:
        break

