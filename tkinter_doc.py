# В этом модуле с помощью библиотеки TKinter мы создаем простейшее графическое приложение для более удобного
# использования скрипта

from tkinter import *
from tkinter import filedialog
import docx_replace as d

def str_to_sort_list(event):
    pattern = ent_pattern.get()
    new_text = ent_new_text.get()
    d.searching_files(path, pattern, new_text)
    lab['text'] = 'Преобразование окончено'

def browse_button():
	global filename
	global path
	path = filedialog.askdirectory()
	filename.set(path)

root = Tk()
filename = StringVar()
lbl1 = Label(master=root,textvariable=filename)
button2 = Button(text="Выбрать папку", command=browse_button)
ent_pattern = Entry(width=20)
ent_new_text = Entry(width=20)
but = Button(text="Преобразовать")
lab = Label(width=20, bg='black', fg='white')

but.bind('<Button-1>', str_to_sort_list)

lbl1.grid(row=0, column=1)
button2.grid(row=0, column=3) 
ent_pattern.grid(row=1, column=1)
ent_new_text.grid(row=2, column=1)
but.grid(row=3, column=1)
lab.grid(row=4, column=1)

root.mainloop()