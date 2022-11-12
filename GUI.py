import tkinter as tk
import numpy as np
import pandas as pd
from scipy import spatial


"""class NewWindow(Toplevel):

    def __init__(self, master=None):

        super().__init__(master=master)
        self.title("New Window")
        self.geometry("200x200")
        label = Label(self, text="This is a new Window")
        label.pack()"""


class AppWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Which Laptop Should I Pick")
        self.root.geometry("450x550")
        root.resizable(width=False, height=False)
        self.__Createselection_menu()

    def __Createselection_menu(self):
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
        self.__Speedclicked = tk.StringVar()
        self.__Speedclicked.set("Choose Speed")
        self.__speed_drop = tk.OptionMenu(
            self.root, self.__Speedclicked, *self.speed_options)
        self.__speed_drop.config(width=10)
        self.__speed_drop.pack(ipadx=10, ipady=15, expand=True)
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
        self.__cpu_drop = tk.OptionMenu(
            self.root, self.CPUclicked, *self.cpu_option)
        self.__cpu_drop.config(width=15)
        self.__cpu_drop.pack(ipadx=10, ipady=10, expand=True)
        ################################################### RAM ##########################################
        self.ram_options = [
            "4 GB",
            "8 GB",
            "16 GB",
            "32 GB"
        ]
        self.RAMclicked = tk.StringVar()
        self.RAMclicked.set("Choose RAM")
        self.__ram_drop = tk.OptionMenu(
            self.root, self.RAMclicked, *self.ram_options)
        self.__ram_drop.config(width=10)
        self.__ram_drop.pack(ipadx=10, ipady=10, expand=True)
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
        self.__storage_drop = tk.OptionMenu(
            self.root,  self.SSDClick, *self.SSD_Option)
        self.__storage_drop.config(width=15)
        self.__storage_drop.pack(ipadx=20, ipady=10, expand=True)
        ####################################################### Storage HDD ###############################################
        self.HDD_Option = ['0', "512", "1000"]
        self.HHDClick = tk.StringVar()
        self.HHDClick.set("Choose HDD Capacity")
        self.__HHD_Drop = tk.OptionMenu(
            self.root, self.HHDClick, *self.HDD_Option)
        self.__HHD_Drop.config(width=15)
        self.__HHD_Drop.pack(ipadx=20, ipady=10, expand=True)
        ################################################## Resolution #################################################
        self.resolution_options = [
            "HD",
            "FHD",
            "2K",
            "4K"
        ]
        self.Resolutionclicked = tk.StringVar()
        self.Resolutionclicked.set("Choose Resolution")
        self.__resolution_drop = tk.OptionMenu(
            self.root, self.Resolutionclicked, *self.resolution_options)
        self.__resolution_drop.config(width=10)
        self.__resolution_drop.pack(ipadx=15, ipady=10, expand=True)
        ################################################### GPU #########################################
        self.__gpu_scale = tk.Scale(self.root, from_=2, to_=9, orient=tk.HORIZONTAL,
                                    tickinterval=1, resolution=0.1, length=200, label="Choose GPU Speed")

        self.__gpu_scale.pack(ipadx=10, ipady=10, expand=True)
        ################################################## Price ###########################################
        self.__pricelabel = tk.Label(self.root, text="Choose Price")
        self.__pricelabel.pack(expand=True)
        self.pricebox = tk.Text(self.root, height=2, width=20)
        self.pricebox.pack(ipadx=10, ipady=10, expand=True)
        ################################################### Claculate #######################################
        self.__btn = tk.Button(self.root, text="Calculate")
        self.__btn.bind("<Button>", lambda e: self.__CreateNewWindow())
        self.__btn.pack(pady=10)

    def __getValue(self):
        # return 0 เมื่ออ่านค่าได้โดยไม่มี error , 1 เมื่อมี error
        if self.__Speedclicked.get() != "Choose Speed":
            self.__speed = self.__Speedclicked.get()
            # ตรงนี้ยังไม่รู้ว่าจะทำให้มันสุ่มเลขขึ้นมายังไงให้มันmatchกับspeedที่user input
            return 0
        else:
            try:
                __processor_score = [1, 2,  3,  5,  7,  9]
                self.__cpu = __processor_score[self.cpu_option.index(
                    self.CPUclicked.get())]

                self.__SSD = int(self.SSDClick.get())/1000

                self.__HDD = int(self.HHDClick.get())/1000

                # HD,FHD,2K,4K
                __resolution_score = [1,  2,  3,  4]

                self.__resolution = __resolution_score[self.resolution_options.index(
                    self.Resolutionclicked.get())]

                __ramgb = [4, 8, 16, 32]
                self.__ram = __ramgb[self.ram_options.index(
                    self.RAMclicked.get())]

                self.__price = float(self.pricebox.get("1.0", tk.END))
                print(self.__price)
                return 0
            except:
                print("Please check your input")
                return 1

    def __CreateNewWindow(self):
        if self.__getValue() == 0:
            newWindow = tk.Toplevel(self.root)
            newWindow.title("New Window")
            newWindow.geometry("200x200")
        else:
            #อยากสร้างหน้าต่างแสดงบอกว่ามี error
            print("Error Occur ")

        return


def calculate_cosine_sim(vector, data):
    similarity = []
    for i in range(0, len(data)):
        similarity.append(
            1-spatial.distance.cosine(vector, data[i]))
    return similarity


mainprogram = AppWindow(tk.Tk())
"""data_to_cal = pd.read_csv("data_Used_ToCal.csv", skipinitialspace=True)
numpydata = data_to_cal.to_numpy()
numpydata = np.delete(numpydata, 0, 1)
df_to_show = pd.read_csv("Laptop_Data.csv", skipinitialspace=True)

# ราคา30k cpu i7 ssd 512 hdd 0 gpuคะแนน5 จอ FHD
similarity = calculate_cosine_sim([3, 7, 0.5, 0, 8, 5, 2], numpydata)
print(df_to_show.loc[similarity.index(max(similarity))])
"""

mainprogram.root.mainloop()
