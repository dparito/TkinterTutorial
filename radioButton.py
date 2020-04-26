import tkinter as tk


root = tk.Tk()

tk_int_var = tk.IntVar()
tk_int_var.set(1)       # initializing the choice to Python

languages = [
    ("C#/.NET"),
    ("Python"),
    ("Swift"),
    ("Java"),
    ("Perl")
]

def ShowChoice():
    print(tk_int_var.get())


tk.Label(root,
         text="""Choose a programming language:""",
         justify=tk.LEFT,
         padx=20).pack()

for val, lang in enumerate(languages):
    tk.Radiobutton(root,
                   text=lang,
                   padx=20,
                   variable=tk_int_var,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)

root.mainloop()