import tkinter as tk
from visual_nets.source.root import SequentialModel
from visual_nets.static.tkinter_constants import *

model = SequentialModel()


class ModelPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Model Page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Start Page",
                  command=lambda: master.switch_frame(StartPage)).pack()
        tk.Button(self, text="Data Page",
                  command=lambda: master.switch_frame(DataPage)).pack()

    def addButtons(self):
        button = tk.Button(self.master, text='Initialize Model', command=lambda: model.create())
        button.pack()

        add = tk.Button(self.master, text='Add Layer', command=lambda: model.addInputLayer())
        add.pack()

        remove = tk.Button(self.master, text='Delete Model', command=lambda: model.removeAllModels())
        remove.pack()


from visual_nets.gui.loaddata import DataPage
from visual_nets.gui.startpage import StartPage
'''
class Applicataion(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.master = master
        self.master.title(TOP_TITLE)
        self.master.geometry(TOP_GEOMETRY)
        self.create_wgts()
        self.addButtons()
'''


