import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd
from scipy import spatial
import random


class AppWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Which Laptop Should I Pick")
        self.root.geometry("450x580")
        root.resizable(width=False, height=False)
        self._processor_score = [1, 2,  3,  5,  7,  9]
        # HD,FHD,2K,4K
        self._resolution_score = [1,  3,  5,  7]
        self._ramgb = [4, 8, 16, 32]
        self._Createselection_menu()

    def _Createselection_menu(self):
        ################################################### Speed ############################################
        self.speed_options = [
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
        self._Speedclicked = tk.StringVar()
        self._Speedclicked.set("Choose Speed")
        self._speed_drop = tk.OptionMenu(
            self.root, self._Speedclicked, *self.speed_options)
        self._speed_drop.config(width=10)
        self._speed_drop.pack(ipadx=10, ipady=15, expand=True)
        ####################################################### CPU ################################################
        self.cpu_option = [
            "Intel Celeron",
            "Intel Pentium,\nAMD Althon",
            "Intel i3,Ryzen 3",
            "Intel i5,Ryzen 5",
            "Intel i7,Ryzen 7",
            "Intel i9,Ryzen 9"
        ]
        self.CPUclicked = tk.StringVar()
        self.CPUclicked.set("Choose CPU")
        self._cpu_drop = tk.OptionMenu(
            self.root, self.CPUclicked, *self.cpu_option)
        self._cpu_drop.config(width=15)
        self._cpu_drop.pack(ipadx=10, ipady=10, expand=True)
        ################################################### RAM ##########################################
        self.ram_options = [
            "4 GB",
            "8 GB",
            "16 GB",
            "32 GB"
        ]
        self.RAMclicked = tk.StringVar()
        self.RAMclicked.set("Choose RAM")
        self._ram_drop = tk.OptionMenu(
            self.root, self.RAMclicked, *self.ram_options)
        self._ram_drop.config(width=10)
        self._ram_drop.pack(ipadx=10, ipady=10, expand=True)
        ####################################################### Storage SSD ############################################
        self.SSD_Option = [
            "0",
            "256",
            "512",
            "1000",
            "2000"
        ]
        self.SSDClick = tk.StringVar()
        self.SSDClick.set("Choose SSD Capacity ")
        self._storage_drop = tk.OptionMenu(
            self.root,  self.SSDClick, *self.SSD_Option)
        self._storage_drop.config(width=15)
        self._storage_drop.pack(ipadx=20, ipady=10, expand=True)
        ####################################################### Storage HDD ###############################################
        self.HDD_Option = ['0', "512", "1000"]
        self.HHDClick = tk.StringVar()
        self.HHDClick.set("Choose HDD Capacity")
        self._HHD_Drop = tk.OptionMenu(
            self.root, self.HHDClick, *self.HDD_Option)
        self._HHD_Drop.config(width=15)
        self._HHD_Drop.pack(ipadx=20, ipady=10, expand=True)
        ################################################## Resolution #################################################
        self.resolution_options = [
            "HD",
            "FHD",
            "2K",
            "4K"
        ]
        self._Resolutionclicked = tk.StringVar()
        self._Resolutionclicked.set("Choose Resolution")
        self._resolution_drop = tk.OptionMenu(
            self.root, self._Resolutionclicked, *self.resolution_options)
        self._resolution_drop.config(width=10)
        self._resolution_drop.pack(ipadx=15, ipady=10, expand=True)
        ################################################### GPU #########################################
        self._gpu_scale = tk.Scale(self.root, from_=2, to_=9, orient=tk.HORIZONTAL,
                                   tickinterval=1, resolution=0.1, length=200, label="Choose GPU Speed")

        self._gpu_scale.pack(ipadx=10, ipady=10, expand=True)
        ################################################## Price ###########################################
        self._pricelabel = tk.Label(self.root, text="Choose Price")
        self._pricelabel.pack(expand=True)
        self._pricebox = tk.Text(self.root, height=2, width=20)
        self._pricebox.pack(ipadx=10, ipady=10, expand=True)
        ################################################### Claculate #######################################
        self._btn = tk.Button(self.root, text="Calculate")
        self._btn.bind("<Button>", lambda e: self._CreateNewWindow())
        self._btn.pack(pady=10)
        ################################################### Clear #######################################
        self._btn = tk.Button(self.root, text="Clear")
        self._btn.bind("<Button>", lambda e: self._Clear())
        self._btn.pack(pady=10)
    def _getValue(self):
        # return 0 เมื่ออ่านค่าได้โดยไม่มี error , 1 เมื่อ userinput speed , 2 เมื่อไม่ได้ input speed และ ใส่ข้อมูลไม่ครบ
        if self._Speedclicked.get() != "Choose Speed":
            self._speed = self._Speedclicked.get()
            self._speed = self.speed_options.index(self._speed)+1
            #NewValue = (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin
            self._cpu = self._processor_score[int(round(
                (((self._speed - 1)*(5-0))/(10-1))+1, 0))]
            self._SSD = int(self.SSD_Option[int(
                ((self._speed-1)*(4-1))/(10-1)+1)])/100
            self._HDD = int(self.HDD_Option[int(
                ((self._speed-1)*(2-0))/(10-1)+0)])/100
            self._resolution = self._resolution_score[int(
                ((self._speed-1)*(3-1))/(10-1)+1)]
            self._ram = self._ramgb[int(
                ((self._speed-1)*(3-0))/(10-1)+0)]
            self._gpu = round((((self._speed-1)*(9-2))/(10-1)
                               )+2+random.uniform(0, 0.6), 1)
            self._price = (((((self._speed-1)*(100000-6000)) /
                           (10-1))+6000)/10000)+round(random.uniform(0, 0.5), 4)
            self.uservector = [self._price,
                               self._cpu, self._SSD, self._HDD, self._ram, self._gpu, self._resolution]

            return 0
        else:
            try:

                self._cpu = self._processor_score[self.cpu_option.index(
                    self.CPUclicked.get())]

                self._SSD = int(self.SSDClick.get())/100

                self._HDD = int(self.HHDClick.get())/100

                self._resolution = self._resolution_score[self.resolution_options.index(
                    self._Resolutionclicked.get())]

                self._ram = self._ramgb[self.ram_options.index(
                    self.RAMclicked.get())]

                self._gpu = self._gpu_scale.get()

                self._price = float(self._pricebox.get("1.0", tk.END))/10000
                self.uservector = [self._price,
                                   self._cpu, self._SSD, self._HDD, self._ram, self._gpu, self._resolution]
                return 0
            except:
                return 1

    def _CreateNewWindow(self):
        readstatus = self._getValue()
        if readstatus == 0:
            newWindow = tk.Toplevel(self.root)
            newWindow.title("Your Laptop")
            newWindow.geometry("450x800")
            similarity = calculate_cosine_sim(self.uservector, numpydata)
            text = df_to_show.loc[similarity.index(
                max(similarity))].to_list()
            col = df_to_show.columns
            a = 0
            c = 1
            string = ""

            for i in text[1:]:
                i = str(i)
                if i != "NaN" and i != "nan":
                    string += str(col[c])+' : '+i+'\n'
                c += 1
            textlabel = tk.Text(newWindow)
            textlabel.insert(tk.END, string)
            textlabel.pack(fill=tk.BOTH, expand=1)
        elif readstatus == 1:
            messagebox.showerror(
                title="Error", message="Please Check Your Input")
            return

    def _Clear(self):
        self._Speedclicked.set("Choose Speed")
        self.CPUclicked.set("Choose CPU")
        self.RAMclicked.set("Choose RAM")
        self.SSDClick.set("Choose SSD Capacity ")
        self.HHDClick.set("Choose HDD Capacity")
        self._Resolutionclicked.set("Choose Resolution")
        self._pricebox.delete('1.0', tk.END)


def calculate_cosine_sim(vector, data):
    similarity = []
    for i in range(0, len(data)):
        similarity.append(
            1-spatial.distance.cosine(vector, data[i]))
    return similarity


mainprogram = AppWindow(tk.Tk())
data_to_cal = pd.read_csv("data_Used_ToCal.csv", skipinitialspace=True)
numpydata = data_to_cal.to_numpy()
numpydata = np.delete(numpydata, 0, 1)
df_to_show = pd.read_csv("Laptop_Data.csv", skipinitialspace=True)


mainprogram.root.mainloop()
