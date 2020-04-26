import tkinter as tk


def var_states():
    print(f"male: {var1_int.get()},\nfemale: {var2_int.get()},\nother: {var3_int.get()}")


root = tk.Tk()

tk.Label(root,
         text="Sex (as many applicable):").grid(row=0, sticky=tk.W)

var1_int = tk.IntVar()
tk.Checkbutton(root,
               text="male",
               variable=var1_int).grid(row=1, sticky=tk.W)

var2_int = tk.IntVar()
tk.Checkbutton(root,
               text="female",
               variable=var2_int).grid(row=2, sticky=tk.W)

var3_int = tk.IntVar()
tk.Checkbutton(root,
               text="other",
               variable=var3_int).grid(row=3, sticky=tk.W)

tk.Button(root,
          text="Quit",
          command=root.quit).grid(row=4, sticky=tk.E, pady=4)

tk.Button(root,
          text="Show",
          command=var_states).grid(row=4, sticky=tk.W, pady=4)

root.mainloop()
