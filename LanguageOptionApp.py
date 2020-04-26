from tkinter import *
from collections import namedtuple

"""
We write an application, which depicts a list of programming languages, e.g. ['Python', 'Ruby', 'Perl', 'C++'] 
and a list of natural languages, e.g. ['English','German'] as checkboxes. So it's possible to choose programming 
languages and natural languages. Furthermore, we have two buttons: A "Quit" button for ending the application and 
a "Peek" button for checking the state of the checkbox variables.
"""


def ShowChoices():
    for prog in prog_languages:
        print(f"{prog.lang}: {prog.var.get()}")
    for nat in natural_languages:
        print(f"{nat.lang}: {nat.var.get()}")

prog_lang_tuple = namedtuple('prog_lang_tuple', ['lang', 'var'])
nat_lang_tuple = namedtuple('nat_lang_tuple', ['lang', 'var'])

prog_var1_int = IntVar()
prog_var2_int = IntVar()
prog_var3_int = IntVar()
prog_var4_int = IntVar()

nat_var1_int = IntVar()
nat_var2_int = IntVar()

prog_languages = [
    prog_lang_tuple(lang="Python", var=prog_var1_int),
    prog_lang_tuple(lang="Ruby", var=prog_var2_int),
    prog_lang_tuple(lang="Perl", var=prog_var3_int),
    prog_lang_tuple(lang="C++", var=prog_var4_int)
]

natural_languages = [
    nat_lang_tuple(lang="English", var=nat_var1_int),
    nat_lang_tuple(lang="German", var=nat_var2_int)
]

root = Tk()
Label(root, text="Choose the languages").grid(row=0, sticky=W)

col_count = 0
for prog in prog_languages:
    Checkbutton(root,
                text=prog.lang,
                variable=prog.var).grid(row=1, column=col_count, sticky=W)
    col_count += 1

col_count = 0
for nat in natural_languages:
    Checkbutton(root,
                text=nat.lang,
                variable=nat.var).grid(row=2, column=col_count, sticky=W)
    col_count += 1

Button(root,
       text="Peek",
       command=ShowChoices).grid(row=2, column=col_count, sticky=W)

col_count += 1

Button(root,
       text="Quit",
       command=root.quit).grid(row=2, column=col_count, sticky=W)

root.mainloop()
