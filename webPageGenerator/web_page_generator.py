
#Imported Modules
import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.master.configure(bg="lightgray")

        # Create a label and an entry widget for user input
        self.label = Label(self.master, text="Enter custom text or click the Default HTML page button", bg="lightgray")
        self.label.grid(row=0, column=0, padx=(10, 0), pady=(10, 10))

        # Create an entry field for the user to input data
        self.entry = Entry(self.master, width=126)
        self.entry.grid(row=1, column=0, columnspan=7, padx=(10, 0))
        
        # Create a button to generate the default HTML page
        self.btn_default = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn_default.grid(row=2, column=5, padx=(10, 10), pady=(20, 10))

        # Create a button to generate the Customer text input
        self.btn_custom = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.generateHTML)
        self.btn_custom.grid(row=2, column=6, padx=(10, 10), pady=(20, 10))

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def generateHTML(self):
        # Get the custom text from the user input
        custom_text = self.entry.get()
        # Create an HTML file with the custom text
        htmlFile = open("index.html", "w")
        htmlContent = f"<html>\n<body>\n<h1>{custom_text}</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        # Open the generated HTML file in a new browser tab
        webbrowser.open_new_tab("index.html")



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
