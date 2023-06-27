import tkinter as tk

def get_input():
    input_text = g.get()
    output_label.config(text=input_text)

# Tworzenie okna
root = tk.Tk()
root.geometry("300x200")
root.title("Wejście użytkownika")

# Tworzenie komponentów GUI
input_label = tk.Label(root, text="Wprowadź tekst:")
input_label.pack()

g = tk.Entry(root)
g.pack()

submit_button = tk.Button(root, text="Wyślij", command=get_input)
submit_button.pack()

output_label = tk.Label(root, text="")
output_label.pack()

# Uruchamianie okna
root.mainloop()