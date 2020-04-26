# TkinterTutorial
SOURCE: https://www.python-course.eu/tkinter_checkboxes.php


# Root widget 
o	Window with a title bar and other decoration provided by the window manager.\
o	Has to be created before any other widget\
o	There can be only one root widget.


# Label widget
o	First parameter – name of the parent window\
o	Keyword param “text” specifies display text\
  	Supports using >1 font within a text\
o	Keyword param “image” – PhotoImage widget\
o	Keyword param “justify” – LEFT/CENTER/RIGHT\
o	Keyword param “padx” – horizontal padding\
o	Keyword param “pady” – vertical padding\
o	Keyword param “compound” – BOTTOM/TOP/LEFT/RIGHT/CENTER  text will be drawn on top of image


# Pack method 
o	tells Tk to fit the size of the window to the given text\
o	Keyword param “side” – left/right/center


# “mainloop”
o	the window won’t appear until we enter the Tk event 
<\br>
<\br>

# PhotoImage widget
o	First parameter = name of the parent window\
o	Keyword parameter “file” – absolute path of the image file
<\br>
<\br>

# Message widget
o	Display short text messages\
o	Provides a multiline object – text may span more than 1 line\
o	Text is automatically broken into lines and justified\
o	Cannot support more than 1 font within a message
<\br>
<\br>

# Button widget
o	Can contain text and images\
o	Display text in only one format, can span >1 line
<\br>
<\br>

# Variable classes:
o	It’s not possible to hand over a regular Python variable to a widget through a variable.\
o	The only kinds of varibales for which this works are variables that are subclasses from a class called “VARIABLE”, defined in the Tkinter module.\
  	x = StringVar()		# default value = “”\
  	x = IntVar()		# default value = 0\
  	x = DoubleVar()		# default value = 0.0\
  	x = BooleanVar()	# returns 0 for False; 1 for True\
  	get() and set() methods to interact with the variables
<\br>
<\br>

# Radio Button widget
o	Can contain text or images\
o	Can only display text in a single font\
o	A Python function or a method can be associated with a radio button\
o	This method will be called when the radio button is pressed\
o	Each group of radio button widgets are associated with the same variable\
o	Pushing a radio button changes the value of that variable\
o	Attribute “indicatoron” = 1/0 
<\br>
<\br>

# CheckBox widget:
o	Can contain only text, in only a single font, or images\
o	Can be associated with a Python function/method\
o	Text can span >1 line
