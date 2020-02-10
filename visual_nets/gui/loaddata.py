import tkinter as tk
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split


class DataPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Data Page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Start Page",
                  command=lambda: master.switch_frame(StartPage)).pack()
        tk.Button(self, text="Model Page",
                  command=lambda: master.switch_frame(ModelPage)).pack()
        self.loadData()

    def loadData(self):
        self.iris = sns.load_dataset('iris').values
        X, y = self.iris[:, 0:4], self.iris[:, 4]
        self.train_test_split(values=X,
                              targets=y,
                              test_ratio=0.1)
        print(self.X_train)
        print(self.y_test)

    def train_test_split(self, values, targets, test_ratio, random_state=10):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(values, targets,
                                                                                test_size=test_ratio,
                                                                                random_state=random_state)


from visual_nets.gui.modelpage import ModelPage
from visual_nets.gui.startpage import StartPage
