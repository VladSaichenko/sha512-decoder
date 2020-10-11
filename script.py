
from tkinter import *
from tkinter import messagebox
import hashlib


hashes = tuple((hashlib.sha512(f'{i}'.encode())).hexdigest() for i in range(1, 1_000_001))

def get_hash_value():
    global hashes
    hash = hashInput.get('1.0', END).strip()
    value = 'Данного хэша нет в базе!'
    for i in range(len(hashes)):
        if hashes[i]==hash:
            value = i+1
            break

    messagebox.showinfo(message=value)

root = Tk()

root.title('sha512 Декодер')
root.geometry('500x250')
root.resizable(width=False, height=True)

canvas = Canvas(root, height=500, width=250)
canvas.pack()

frame = Frame(root, bg='gray')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

btn = Button(frame, text='Анализировать', bg='white', command=get_hash_value)
btn.pack()

hashInput = Text(frame, bg='white')
hashInput.pack()

root.mainloop()
