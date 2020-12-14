from tkinter import *
from tkinter import filedialog
from tkinter import font

#tkinter window
root = Tk()
root.title("Santi's Text Editor")
root.geometry("1200x660")
root.iconbitmap(r'textIcon.ico')

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



root.mainloop()