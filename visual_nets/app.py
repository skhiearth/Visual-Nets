import tkinter as tk
from visual_nets.gui.startpage import StartPage
from visual_nets.static.tkinter_constants import *


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        self.title(TOP_TITLE)
        self.geometry(TOP_GEOMETRY)
        self.create_widgets()

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def create_widgets(self):
        MainMenu = tk.Menu(self.master)
        self.config(menu=MainMenu)

        filemenu = tk.Menu(MainMenu)
        helpmenu = tk.Menu(MainMenu)

        filemenu.add_command(label='New')
        filemenu.add_command(label='Open')
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.quit)
        MainMenu.add_cascade(label='File', menu=filemenu)

        helpmenu.add_command(label='About')
        MainMenu.add_cascade(label='Help', menu=helpmenu)


app = Application()
app.mainloop()
