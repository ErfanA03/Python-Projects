#Import Modules
from tkinter import *
import tkinter as tk
from tkinter import messagebox

#Import our other Modules
import student_tracking_main
import student_tracking_func



def load_gui(self):
    """
        Creating a function to load our widgets when called in "student_tracking_main"
        We're also using grid manager to place the widgets.
    """
    #Labels
    self.lbl_fname = tk.Label(self.master,text='First Name:', fg='white', bg="#0a106e")
    self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    
    self.lbl_lname = tk.Label(self.master,text='Last Name:', fg='white', bg="#0a106e")
    self.lbl_lname.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    
    self.lbl_phone = tk.Label(self.master,text='Phone Number:', fg='white', bg="#0a106e")
    self.lbl_phone.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    
    self.lbl_email = tk.Label(self.master,text='Email Address:', fg='white', bg="#0a106e")
    self.lbl_email.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    
    self.lbl_course = tk.Label(self.master,text='Current Course:', fg='white', bg="#0a106e")
    self.lbl_course.grid(row=8,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    
    self.lbl_info = tk.Label(self.master,text='Information:', fg='white', bg="#0a106e")
    self.lbl_info.grid(row=0,column=2,padx=(0,0),pady=(10,0),sticky=N+W)

    #Text Fields
    self.txt_fname = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    
    self.txt_lname = tk.Entry(self.master,text='')
    self.txt_lname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    self.txt_phone = tk.Entry(self.master,text='')
    self.txt_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    self.txt_email = tk.Entry(self.master,text='')
    self.txt_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    self.txt_course = tk.Entry(self.master,text='')
    self.txt_course.grid(row=9,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    
    #Define the listbox with a scrollbar and grid them
    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
    
    self.lstList1.bind('<<ListboxSelect>>',lambda event: student_tracking_func.onSelect(self,event))
    self.scrollbar1.config(command=self.lstList1.yview)
    
    self.scrollbar1.grid(row=1,column=5,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
    self.lstList1.grid(row=1,column=2,rowspan=7,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)
    
    #All our buttons(Submit,Update,Delete,Close)
    self.btn_submit = tk.Button(self.master,width=12,height=2,text='Submit',command=lambda: student_tracking_func.onSubmit(self))
    self.btn_submit.grid(row=10,column=0,padx=(25,0),pady=(45,10),sticky=W)
    
    self.btn_update = tk.Button(self.master,width=12,height=2,text='Update',command=lambda: student_tracking_func.onUpdate(self))
    self.btn_update.grid(row=10,column=1,padx=(15,0),pady=(45,10),sticky=W)
    
    self.btn_delete = tk.Button(self.master,width=12,height=2,text='Delete',command=lambda: student_tracking_func.onDelete(self))
    self.btn_delete.grid(row=10,column=2,padx=(15,0),pady=(45,10),sticky=W)
    
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: student_tracking_func.ask_quit(self))
    self.btn_close.grid(row=10,column=4,columnspan=1,padx=(15,0),pady=(45,10),sticky=E)
    
    student_tracking_func.create_db(self)
    student_tracking_func.onRefresh(self)


    
if __name__ == "__main__":
    pass
