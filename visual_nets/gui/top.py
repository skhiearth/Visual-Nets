import tkinter
from visual_nets.source.root import SequentialModel

model = SequentialModel()


class Application(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.master = master
        self.master.title('Visual Nets')
        self.master.geometry("256x160")
        self.create_wgts()
        self.addButtons()

    def addButtons(self):
        button = tkinter.Button(self.master, text='Initialize Model', command=lambda: model.create())
        button.pack()

        add = tkinter.Button(self.master, text='Add Layer', command=lambda: model.addInputLayer())
        add.pack()

        remove = tkinter.Button(self.master, text='Delete Model', command=lambda: model.removeAllModels())
        remove.pack()

    def create_wgts(self):
        MainMenu = tkinter.Menu(self.master)
        self.master.config(menu=MainMenu)

        filemenu = tkinter.Menu(MainMenu)
        helpmenu = tkinter.Menu(MainMenu)

        filemenu.add_command(label='New')
        filemenu.add_command(label='Open')
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.master.quit)
        MainMenu.add_cascade(label='File', menu=filemenu)

        helpmenu.add_command(label='About')
        MainMenu.add_cascade(label='Help', menu=helpmenu)


top = tkinter.Tk()
app = Application(master=top)
app.mainloop()
