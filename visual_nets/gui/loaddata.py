import tkinter as tk


class DataPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Data Page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Start Page",
                  command=lambda: master.switch_frame(StartPage)).pack()
        tk.Button(self, text="Model Page",
                  command=lambda: master.switch_frame(ModelPage)).pack()


from visual_nets.gui.modelpage import ModelPage
from visual_nets.gui.startpage import StartPage
