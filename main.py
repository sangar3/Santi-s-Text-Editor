from tkinter import *
from tkinter import filedialog
from tkinter import font

#tkinter window
root = Tk()
root.title("Santi's Text Editor")
root.geometry("1200x660")
root.iconbitmap(r'textIcon.ico')

#Global vars
global open_status_name
open_status_name = False

global selected
selected = False

#FUNCTIONS

#Create New File Functions
def new_file():
    # DEL Prev Text
    my_text.delete("1.0",END)
    #Update Status Bar
    root.title('New File -Santi\'s Text Editor')
    status_bar.config(text="New File      ")

    global open_status_name
    open_status_name = False

def open_file():
    #DEL Prev Text
    my_text.delete("1.0", END)

    #Grab certain Filename
    text_file = filedialog.askopenfilename(initialdir="C:/Python/Santi-s-Text-Editor",  title="Open File",
                                       filetypes=(("Text Files","*.txt"),("HTML Files","*.html"),("All Files","*.*") ))
    #Checking if there is filename
    if text_file:
        #global filename
        global open_status_name
        open_status_name = text_file

    #Update Status Bars
    name = text_file
    status_bar.config(text=f'{name}       ')
    name = name.replace("C:/Python/Santi-s-Text-Editor/","")
    root.title(f'{name} - Santi\'s Text Editor')

    #Open the file
    text_file = open(text_file, 'r')
    FileContent = text_file.read()
    #Add file to Textbox
    my_text.insert(END,FileContent)
    #Closed the opened file
    text_file.close()

def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/Python/Santi-s-Text-Editor",
                                             title="Save File",filetypes=(("Text Files","*.txt"),
                                                                          ("HTML Files","*.html"),("All Files","*.*") ))
    if text_file:
        #Update Status Bars
        name = text_file
        status_bar.config(text=f'Saved:{name}       ')
        name = name.replace("C:/Python/Santi-s-Text-Editor/","")
        root.title(f'{name} - Santi\'s Text Editor')

        # Save the file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))  # Grabbing file content
        # close the file
        text_file.close()

def save_file():
    global open_status_name
    if open_status_name:
        # Save the file
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))  # Grabbing file content
        # close the file
        text_file.close()
        #add pop up when file is saved
        status_bar.config(text=f'Saved:{open_status_name}       ')
    else:
        save_as_file()

#e = event

def cut_text(e):
    global selected
    # check if we used keyboard shortcuts
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            #Grab selected text from text box
            selected = my_text.selection_get()

            #delete Selected Text From text box from first to last
            my_text.delete("sel.first","sel.last")
            # Clear the clipboard then append
            root.clipboard_clear()
            root.clipboard_append(selected)

def copy_text(e):
    global selected
    # check if we used keyboard shortcuts
    if e:
        selected = root.clipboard_get()
    if my_text.selection_get():
        # Grab selected text from text box
        selected = my_text.selection_get()
        #Clear the clipboard then append
        root.clipboard_clear()
        root.clipboard_append(selected)

def paste_text(e):
    global selected
    # check if we used keyboard shortcuts
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position,selected)

#Create Main Frame
my_frame = Frame(root)

my_frame.pack(pady=5)

#Create Scrollbar for Text Box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#Create Text Box

#Text Widget
my_text = Text(my_frame, width=97, height=25,
               font=("Montserrat",16), selectbackground="yellow", selectforeground="black", undo=True,
               yscrollcommand=text_scroll.set)

#configure our Scrollbar
text_scroll.config(command=my_text.yview)

my_text.pack()

#Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

#Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut                 Ctrl+X", command=lambda: cut_text(False))
edit_menu.add_command(label="Copy                Ctrl+C", command=lambda: copy_text(False))
edit_menu.add_command(label="Paste               Ctrl+V", command=lambda: paste_text(False))
edit_menu.add_command(label="Undo                Ctrl+Z")
edit_menu.add_command(label="Redo                Ctrl+Shift+Z")

#Add Status Bar at bottom
status_bar = Label(root,text='Ready        ',anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=5)

#Edit binding
root.bind('<Control-x>',cut_text)
root.bind('<Control-c>',copy_text)
root.bind('<Control-v>',paste_text)

#Main Loop of App
root.mainloop()