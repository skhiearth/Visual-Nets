import tkinter as tk


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Start page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Data Page",
                  command=lambda: master.switch_frame(DataPage)).pack()
        tk.Button(self, text="Model Page",
                  command=lambda: master.switch_frame(ModelPage)).pack()


from visual_nets.gui.loaddata import DataPage
from visual_nets.gui.modelpage import ModelPage
