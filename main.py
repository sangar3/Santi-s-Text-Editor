from tkinter import *
from tkinter import filedialog
from tkinter import font

#tkinter window
root = Tk()
root.title("Santi's Text Editor")
root.geometry("1200x660")
root.iconbitmap(r'textIcon.ico')

#FUNCTIONS

#Create New File Functions
def new_file():
    # DEL Prev Text
    my_text.delete("1.0",END)
    #Update Status Bar
    root.title('New File -Santi\'s Text Editor')
    status_bar.config(text="New File      ")


def open_file():
    #DEL Prev Text
    my_text.delete("1.0", END)

    #Grab certain Filename
    text_file = filedialog.askopenfilename(initialdir="C:/Python/Santi-s-Text-Editor",  title="Open File",
                                       filetypes=(("Text Files","*.txt"),("HTML Files","*.html"),("All Files","*.*") ))
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

#Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As")
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)


#Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")




#Add Status Bar at bottom
status_bar = Label(root,text='Ready        ',anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=5)




root.mainloop()