from tkinter import *
from tkinter import ttk
import numpy as np
import pandas as pd
from scipy import spatial


class NewWindow(Toplevel):

    def __init__(self, master=None):

        super().__init__(master=master)
        self.title("New Window")
        self.geometry("200x200")
        label = Label(self, text="This is a new Window")
        label.pack()


def calculate_cosine_sim(vector, data):
    similarity = []
    for i in range(0, len(data)):
        similarity.append(
            1-spatial.distance.cosine(vector, data[i]))
    return similarity


root = Tk()
data_to_cal = pd.read_csv("data_Used_ToCal.csv", skipinitialspace=True)
numpydata = data_to_cal.to_numpy()
numpydata = np.delete(numpydata, 0, 1)


root.title("Which Laptop Should I Pick")
root.geometry("450x450")


def display_text():
    global entry
    string = entry.get()
    label.configure(text=string)

# Change the label text


def show():
    label.config(text=clicked.get())

# New window


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
clicked.set("Choose Speed")
drop = OptionMenu(root, clicked, *speed_options)
drop.config(width=10)
drop.pack(ipadx=10, ipady=10, expand=True)

####################################################### CPU ################################################
cpu_option = [
    "Intel Celeron",
    "Intel Pentium,\nAMD Althon",
    "Intel i3,Ryzen 3",
    "Intel i5,Ryzen 5",
    "Intel i7,Ryzen 7",
    "Intel i9,Ryzen 9"
]
clicked = StringVar()
clicked.set("Choose CPU")
drop = OptionMenu(root, clicked, *cpu_option)
drop.config(width=15)
drop.pack(ipadx=10, ipady=10, expand=True)

drop.pack()
####################################################### Storage ############################################
storage_options = [
    "SSD",
    "SSD & HDD",
    "HDD"
]
clicked = StringVar()
clicked.set("Choose Storage")
drop = OptionMenu(root, clicked, *storage_options)
drop.config(width=10)
drop.pack(ipadx=10, ipady=10, expand=True)
drop.pack()

################################################## Resolution #################################################
resolution_options = [
    "HD",
    "FHD",
    "2K",
    "4K"
]
clicked = StringVar()
clicked.set("Choose Resolution")
drop = OptionMenu(root, clicked, *resolution_options)
drop.config(width=10)
drop.pack(ipadx=15, ipady=10, expand=True)


################################################### RAM ##########################################
ram_options = [
    "4 GB",
    "8 GB",
    "16 GB",
    "32 GB"
]
clicked = StringVar()
clicked.set("Choose RAM")
drop = OptionMenu(root, clicked, *ram_options)
drop.config(width=10)
drop.pack(ipadx=10, ipady=10, expand=True)
drop.pack()


################################################### GPU #########################################
gpu_scale = Scale(root, from_=2, to_=9, orient=HORIZONTAL,
                  tickinterval=1, resolution=0.1, length=200, label="GPU Speed")

gpu_scale.pack(ipadx=10, ipady=10, expand=True)


################################################### Claculate #######################################
# a button widget which will
# open a new window on button click
btn = Button(root, text="Calculate")
df_to_show = pd.read_csv("Laptop_Data.csv", skipinitialspace=True)

# ราคา30k cpu i7 ssd 512 hdd 0 gpuคะแนน5 จอ FHD
similarity = calculate_cosine_sim([3, 7, 0.5, 0, 8, 5, 2], numpydata)
print(df_to_show.loc[similarity.index(max(similarity))])
del similarity, df_to_show
# Following line will bind click event
# On any click left / right button
# of mouse a new window will be opened
btn.bind("<Button>",
         lambda e: NewWindow(root))

btn.pack(pady=10)
# Create Label
label = Label(root, text=" ")
label.pack()


# Execute tkinter
root.mainloop()
