import locale
locale.setlocale(locale.LC_ALL, "UZ_uz")
from tkinter import *
from tkinter.ttk import *
from time import strftime

# creating tkinter window
root = Tk()
root.geometry("600x100")
root.title('Clock')
root.config(background='black')


def show_time():
    string = strftime('%H:%M:%S %A')
    lbl.config(text=string)
    lbl.after(1000, show_time)


# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font=('Mono', 40, 'italic'),
            background='black',
            foreground='red' )

# PLacing clock at the centre
# of the tkinter window
lbl.pack(anchor='center')
show_time()
mainloop()