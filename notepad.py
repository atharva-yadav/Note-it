from tkinter import *
import tkinter.messagebox as tkmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textArea.delete(1.0, END)
        f = open(file, "r")
        textArea.insert(1.0, f.read())
        f.close()


def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(textArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(textArea.get(1.0, END))
        f.close()


def cut():
    textArea.event_generate("<<Cut>>")


def copy():
    textArea.event_generate("<<Copy>>")


def paste():
    textArea.event_generate("<<Paste>>")


def time():
    from datetime import datetime
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)


def viewHelp():
    tkmsg.showinfo(
        "Dev Support", "For any query, Please visit Tkinter official site   https://tkdocs.com/ ")


def giveFeedback():
    feedback = tkmsg.askquestion(
        "Dev Feedback", "Have you enjoyed our app? Let us know..")
    if feedback == "yes":
        tkmsg.showinfo(
            "Feedback", "Thanks for reviewing us. If possible please rate us on App Store Also")
    else:
        tkmsg.showinfo(
            "Feedback", "Ohh..Sorry for Inconvinience.  What went wrong? Contact our team at  https://tkdocs.com/ ")

    print(feedback)


def aboutNoteIt():
    tkmsg.showinfo(
        "About Note It", "Note It\n\nVersion 20A1 (1.0.0)\n©TechProgrammer - All Rights reserved\n\nThis Product licenced under github.com/atharva-yadav")


root = Tk()
root.title("Untitled - Note It")
root.geometry("800x650")
root.wm_iconbitmap("icon.ico")
root.config(background="thistle1")

# Creating textarea
textArea = Text(root, font="BahnschriftSemiBold 12", bg="ghost white", padx=5, pady=5)
# expand attribute expands text area over whole window
textArea.pack(fill=BOTH, expand=TRUE)
file = None

# Main horizontal menubar
MenuBar = Menu(root)

# Creating submenu "File"
FileMenu = Menu(MenuBar, tearoff=0)
FileMenu.add_command(label="New", command=newFile)
FileMenu.add_command(label="Open File...", command=openFile)
FileMenu.add_separator()
FileMenu.add_command(label="Save", command=save)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=quit)
# Cascading all in "File"
MenuBar.add_cascade(label="File", menu=FileMenu)


# Creating submenu "Edit"
EditMenu = Menu(MenuBar, tearoff=0)
# EditMenu.add_separator()
EditMenu.add_command(label="Cut", command=cut)
EditMenu.add_command(label="Copy", command=copy)
EditMenu.add_command(label="Paste", command=paste)
EditMenu.add_separator()
EditMenu.add_command(label="Time", command=time)
# Cascading all in "Edit"
MenuBar.add_cascade(label="Edit", menu=EditMenu)


# Creating submenu "Help"
HelpMenu = Menu(MenuBar, tearoff=0)
HelpMenu.add_command(label="View Help", command=viewHelp)
HelpMenu.add_command(label="Give Feedback", command=giveFeedback)
HelpMenu.add_separator()
HelpMenu.add_command(label="About Note It", command=aboutNoteIt)
# Cascading all in "Help"
MenuBar.add_cascade(label="Help", menu=HelpMenu)


# Creating submenu "Exit App"
MenuBar.add_separator()
MenuBar.add_command(label="Exit App", command=quit)

# Adding a scrollbar
yScroll = Scrollbar(textArea)
yScroll.pack(fill=Y, side=RIGHT)

yScroll.config(command=textArea.yview)
textArea.config(yscrollcommand=yScroll.set)


root.config(menu=MenuBar)

statusvar = StringVar()
statusvar.set("© Note It by TechProgrammer")

sbar = Label(root, textvariable=statusvar, relief=GROOVE, anchor="w" )
sbar.pack(side="bottom",fill="x")

root.mainloop()
