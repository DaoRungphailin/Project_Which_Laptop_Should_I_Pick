from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Which Laptop Should I Pick")
root.geometry( "400x400" )

def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)

# Change the label text
def show():
	label.config( text = clicked.get() )

################################################### Speed ############################################
speed_options = [
	"Level 1",
	"Level 2",
	"Level 3",
	"Level 4",
	"Level 5",
	"Level 6",
	"Level 7",
    "Level 8",
    "Level 9",
    "Level 10"
]
clicked = StringVar()
clicked.set( "Choose Speed" )
drop = OptionMenu( root , clicked , *speed_options )
drop.pack()


####################################################### Storage ############################################
storage_options = [
	"SSD",
    "SSD & HDD",
    "HDD"
]
clicked = StringVar()
clicked.set( "Choose Storage")
drop = OptionMenu( root , clicked , *storage_options )
drop.pack()

################################################## Resolution #################################################
resolution_options = [
	"HD",
    "FHD",
    "2K",
    "4K"
]
clicked = StringVar()
clicked.set( "Choose Resolution")
drop = OptionMenu( root , clicked , *resolution_options )
drop.pack()


################################################### RAM ##########################################
l = Label(root, text = "RAM")
l.config(font =("Courier", 14))
l.pack()

label=Label(root, text="", font=("Courier 22 bold"))
label.pack()

entry= Entry(root, width= 40)
entry.focus_set()
entry.pack()
ttk.Button(root, text= "save",width= 20, command= display_text).pack(pady=20)


################################################### GPU #########################################
l = Label(root, text = "GPU")
l.config(font =("Courier", 14))
l.pack()

entry= Entry(root, width= 40)
entry.focus_set()
entry.pack()
ttk.Button(root, text= "save",width= 20, command= display_text).pack(pady=20)

################################################### Claculate #######################################
# Create button, it will change label text
button = Button( root , text = "calculate" , command = show ).pack()

# Create Label
label = Label( root , text = " " )
label.pack()


# Execute tkinter
root.mainloop()
