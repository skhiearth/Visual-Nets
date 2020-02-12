import tkinter as tk
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from pandastable import Table
from tkinter import filedialog


class DataPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.create_frames()

        tk.Label(self.topFrame, text="Data Page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.bottomFrame, text="Start Page",
                  command=lambda: master.switch_frame(StartPage)).pack(fill="x")
        tk.Button(self.rightFrame, text="Load Data",
                  command=lambda: self.loadData()).pack()
        tk.Button(self.leftFrame, text="test",
                  command=lambda: self.loadData()).pack()
        '''
        tk.Button(self.topFrame, text="Create Model",
                  #command=lambda: master.switch_frame(ModelPage)).pack()
        '''

    def create_frames(self):
        self.topFrame = tk.Frame(self, padx=10, pady=10, bg="blue")
        self.topFrame.pack(side=tk.TOP, fill="x")

        self.bottomFrame = tk.Frame(self, height=100, padx=10, pady=10, bg="yellow")
        self.bottomFrame.pack(side=tk.BOTTOM, fill="x")

        self.leftFrame = tk.Frame(self, padx=10, pady=10, bg="red")
        self.leftFrame.pack(side=tk.LEFT, fill="both", expand=True)

        self.rightFrame = tk.Frame(self, padx=10, pady=10, bg="green", width=350)
        self.rightFrame.pack(side=tk.RIGHT, fill="both", expand=True)

        self.tableFrame = tk.Frame(self.rightFrame, height=250)
        self.tableFrame.pack(side=tk.BOTTOM, expand=False, fill="x")

    def loadData(self):
        filepath = filedialog.askopenfilename(initialdir="/", title="Select data file",
                                              filetypes=(("CSV Files", "*.csv"), ("all files", "*.*")))
        self.df = pd.read_csv(filepath)
        self.dfValues = self.df.values
        X, y = self.dfValues[:, 0:4], self.dfValues[:, 4]
        tk.Button(self, text="Split Data",
                  command=lambda: self.train_test_split(values=X,
                                                        targets=y,
                                                        test_ratio=0.1)).pack()
        self.showTable(data=self.df)

    def showTable(self, data):
        pt = Table(self.tableFrame, dataframe=data, showstatusbar=True).show()

    def train_test_split(self, values, targets, test_ratio, random_state=10):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(values, targets,
                                                                                test_size=test_ratio,
                                                                                random_state=random_state)


from visual_nets.gui.modelpage import ModelPage
from visual_nets.gui.startpage import StartPage
