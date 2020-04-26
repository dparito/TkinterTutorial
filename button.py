import tkinter as tk


def write_slogan():
    whatever_you_do = "Whatever you do will be insignificant, but it is important that you do it. \n(Mahatma Gandhi)"
    msg = tk.Message(frame,
                     text=whatever_you_do,
                     bg="light green",
                     font="times 24 italic")
    msg.pack()

counter = 0
def counter_label(my_label: tk.Label) -> None:
    def count():
        global counter
        counter += 1
        my_label.config(text=str(counter))
        my_label.after(1000, count)

    count()


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame, fg="green")
label.pack()
counter_label(label)
button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)

slogan = tk.Button(frame,
                   text="Hello",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()
