import tkinter as tk
from visual_nets.static.nonbmp import *

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.create_frames()

    def create_frames(self):
        self.topFrame = tk.Frame(self, padx=10, pady=10)
        self.topFrame.pack(side=tk.TOP, fill="x")

        self.bottomFrame = tk.Frame(self, height=100, padx=10, pady=10)
        self.bottomFrame.pack(side=tk.BOTTOM, fill="x")

        self.leftFrame = tk.Frame(self, padx=10, pady=10, bg="red")
        self.leftFrame.pack(side=tk.LEFT, fill="both", expand=True)

        self.rightFrame = tk.Frame(self, padx=10, pady=10, bg="green", width=350)
        self.rightFrame.pack(side=tk.RIGHT, fill="both", expand=False)

        self.wig_create()

    def wig_create(self):
        tk.Label(self.topFrame, text="Visual Nets", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.bottomFrame, text="Data Page",
                  command=lambda: self.master.switch_frame(DataPage)).pack()

        em = with_surrogates('\U0001f64f')

        tk.Label(self.bottomFrame, text="Created by skhiearth", font=('Helvetica', 12)).pack(side="top", fill="x", pady=3)


from visual_nets.gui.loaddata import DataPage
