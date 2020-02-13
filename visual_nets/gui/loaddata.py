import tkinter as tk
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from pandastable import Table
from tkinter import filedialog
from visual_nets.static.tkinter_constants import *


class DataPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.scalingType = tk.IntVar()
        self.scalingType.set(0)  # No Scaling

        self.create_frames()
        self.create_widgets()

    def create_frames(self):
        self.topFrame = tk.Frame(self, padx=10, pady=10, bg="blue")
        self.topFrame.pack(side=tk.TOP, fill="x")

        self.bottomFrame = tk.Frame(self, height=100, padx=10, pady=10, bg="yellow")
        self.bottomFrame.pack(side=tk.BOTTOM, fill="x")

        self.leftFrame = tk.Frame(self, padx=10, pady=10, bg="red")
        self.leftFrame.pack(side=tk.LEFT, fill="both", expand=True)

        self.rightFrame = tk.Frame(self, padx=10, pady=10, bg="green", width=350)
        self.rightFrame.pack(side=tk.RIGHT, fill="both", expand=False)

        self.tableFrame = tk.Frame(self.rightFrame, height=250, width=300, padx=10, pady=10)
        self.tableFrame.pack(side=tk.BOTTOM, expand=False)

        self.tableContainerFrame = tk.Frame(self.tableFrame, height=200)
        self.tableContainerFrame.pack(side=tk.BOTTOM, expand=False, fill="x")

    def create_widgets(self):
        tk.Label(self.tableFrame, text='Feature Scaling: ',
                 font=('Helvetica', 11)).pack(anchor=tk.W)

        for val, ty in enumerate(SCALING_TYPES):
            tk.Radiobutton(self.tableFrame,
                           text=ty,
                           font=('Helvetica', 11),
                           padx=8,
                           command=self.scaleData,
                           variable=self.scalingType,
                           value=val).pack(anchor=tk.W)

        tk.Label(self.topFrame, text="Data Page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.bottomFrame, text="Start Page",
                  command=lambda: self.master.switch_frame(StartPage)).pack(fill="x")
        tk.Button(self.rightFrame, text="Load Data",
                  command=lambda: self.loadData()).pack()
        tk.Button(self.leftFrame, text="test",
                  command=lambda: self.loadData()).pack()
        '''
        tk.Button(self.topFrame, text="Create Model",
                  #command=lambda: master.switch_frame(ModelPage)).pack()
        '''

    def loadData(self):
        filepath = filedialog.askopenfilename(initialdir="/",
                                              title="Select data file",
                                              filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
        self.originalDf = pd.read_csv(filepath)
        self.df = self.originalDf
        self.dfValues = self.df.values
        self.splitData(values=self.dfValues)
        self.showTable(data=self.df)

    def scaleData(self):
        print(self.scalingType.get())
        if self.scalingType.get() == 0:
            self.df = self.originalDf
            self.showTable(data=self.df)

        elif self.scalingType.get() == 1:
            minMaxScaler = preprocessing.MinMaxScaler()
            self.df = minMaxScaler.fit_transform(self.df)
            self.showTable(data=self.df)

        elif self.scalingType.get() == 2:
            robustScaler = preprocessing.RobustScaler()
            self.df = robustScaler.fit_transform(self.df)
            self.showTable(data=self.df)

        elif self.scalingType.get() == 3:
            standardScaler = preprocessing.StandardScaler()
            self.df = standardScaler.fit_transform(self.df)
            self.showTable(data=self.df)


    def splitData(self, values):
        X, y = self.dfValues[:, 0:4], self.dfValues[:, 4]
        tk.Button(self, text="Split Data",
                  command=lambda: self.train_test_split(values=X,
                                                        targets=y,
                                                        test_ratio=0.1)).pack()

    def showTable(self, data):
        pt = Table(self.tableContainerFrame, dataframe=data, showstatusbar=True).show()
        tk.Label(self.tableFrame, text="Total null values: {}".format(data.isna.sum()),
                 font=('Helvetica', 11)).pack(anchor=tk.W)

    def train_test_split(self, values, targets, test_ratio, random_state=10):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(values, targets,
                                                                                test_size=test_ratio,
                                                                                random_state=random_state)


from visual_nets.gui.modelpage import ModelPage
from visual_nets.gui.startpage import StartPage
