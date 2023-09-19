#Import Modules
from tkinter import *
import tkinter as tk
from tkinter import messagebox

#Import our other Modules
import student_tracking_gui
import student_tracking_func


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(600,450) #(Height, Width)
        self.master.maxsize(600,450)
        # This CenterWindow method will center our app on the user's screen
        student_tracking_func.center_window(self,600,450)
        self.master.title("Student Tracking")
        self.master.configure(bg="#0a106e")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_tracking_func.ask_quit(self))
        arg = self.master
        
        # load in the GUI widgets from a separate module, 
        # keeping your code comparmentalized and clutter free
        student_tracking_gui.load_gui(self)
        
        # Instantiate the Tkinter menu dropdown object
        # This is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: student_tracking_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) # defines the particular drop down colum and tearoff=0 means do not separate from menubar
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Student Tracker App") # add_command is a child menubar item of the add_cascde parent item
        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)
        """
            Finally, we apply the config method of the widget to display the menu
            From here we could also pass in additional aprams for additional 
            functionality or appearances such as a borderwidth.
        """
        self.master.config(menu=menubar, borderwidth='1')

        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
