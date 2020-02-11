import tkinter as tk
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from pandastable import Table


class DataPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        bottomFrame = tk.Frame(self.master, height=100)
        bottomFrame.pack(side=tk.BOTTOM, fill="x")

        tk.Label(self, text="Data Page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(bottomFrame, text="Start Page",
                  command=lambda: master.switch_frame(StartPage)).pack(fill="x")
        tk.Button(self, text="Load Data",
                  command=lambda: self.loadData()).pack()
        tk.Button(self, text="Create Model",
                  command=lambda: master.switch_frame(ModelPage)).pack()

    def loadData(self):
        self.iris = sns.load_dataset('iris')
        self.df = sns.load_dataset('iris').values
        X, y = self.df[:, 0:4], self.df[:, 4]
        tk.Button(self, text="Split Data",
                  command=lambda: self.train_test_split(values=X,
                                                        targets=y,
                                                        test_ratio=0.1)).pack()
        self.showTable(data=self.iris)

    def showTable(self, data):
        f = tk.Frame(self)
        f.pack(fill=tk.BOTH, expand=1)
        pt = Table(f, dataframe=data, showstatusbar=True).show()

    def train_test_split(self, values, targets, test_ratio, random_state=10):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(values, targets,
                                                                                test_size=test_ratio,
                                                                                random_state=random_state)


from visual_nets.gui.modelpage import ModelPage
from visual_nets.gui.startpage import StartPage
