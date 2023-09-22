
from tkinter import *

# Pack Managers:
"""
# With pack geometry manager

win = Tk()
b1 = Button(win, text="One")
b2 = Button(win, text="Two")
b1.pack(side=LEFT, padx = 10)
b2.pack(side=LEFT, padx = 10)


# With grid geometry manager

win = Tk()
b1 = Button(win, text="One")
b2 = Button(win, text="Two")
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)

# A "Label" widget is used to place text into the window
l = Label(win, text="This is a label")
l.grid(row=1, column=0)
"""

#Buttons:
"""
win = Tk()
f = Frame(win)
b1 = Button(f, text="One")
b2 = Button(f, text="Two")
b3 = Button(f, text="Three")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
l = Label(win, text="This label is over all buttons")
l.pack()
f.pack()

# The configure method
b1.configure(text="Uno")

# Buttons are tied to callback functions
def but1():
    print("Button one was pushed")

b1.configure(command=but1)
"""

#Text-Fields/Entries:
"""
win = Tk()
v = StringVar() #Allows us to set 'v' to a string value.
e = Entry(win, textvariable = v)
e.pack()
v.get() #Gets data
v.set("this is set by the program") #Sets data
"""

#Listbox:
win = Tk()
lb = Listbox(win, height=3) # 'height' parameter limits how many lines will show.
lb.pack()
lb.insert(END, "first entry")
lb.insert(END, "second entry")
lb.insert(END, "third entry")
lb.insert(END, "fourth entry")


#Scroll Bar:
sb = Scrollbar(win, orient=VERTICAL)
sb.pack(side=LEFT, fill=Y)

#Add functionality to scroll bar, right now it doesn't do anything
#This is because that neither the listbox or scrollbar know about the other:
sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)
print(lb.curselection())










