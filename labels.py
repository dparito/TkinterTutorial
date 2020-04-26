import tkinter as tk

root = tk.Tk()

# HEADER TEXT
label_text = tk.Label(root, text="Hello Tkinter!")
label_text.pack()

# COLORIZED LABELS
tk.Label(root,
         text="Red text in Times",
         fg="red",
         font="Times").pack()
tk.Label(root,
         text="Blue text in Verdana/B/U",
         fg="blue",
         bg="yellow",
         font="Verdana 10 bold underline").pack()
tk.Label(root,
         text="Green text in Helvetica/I",
         fg="light green",
         bg="dark green",
         font="Helvetica 16 italic").pack()

# DYNAMIC LABEL CONTENT
counter = 0
def counter_label(my_label: tk.Label) -> None:
    def count():
        global counter
        counter += 1
        my_label.config(text=str(counter))
        my_label.after(1000, count)

    count()


root.title("Counting Seconds")
label = tk.Label(root, fg="green")
label.pack()
counter_label(label)
button = tk.Button(root,
                   text="STOP",
                   width=25,
                   command=root.destroy)
button.pack()

# IMAGE WITH EXPLANATION
logo = tk.PhotoImage(file="naluLogo.png")
explanation = """Trying to add additional text to support 
the image. This text should appear 
on the left side of the image.
At present, only GIF, PNG and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""
label_image_exp = tk.Label(root,
                           justify=tk.LEFT,
                           compound=tk.LEFT,
                           padx=10,
                           text=explanation,
                           image=logo).pack(side="right")

root.mainloop()
