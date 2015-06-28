import Tkinter as tk
from ScrolledText import ScrolledText

class textpad(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.st = ScrolledText()
        self.st.pack()

        self.menubar = tk.Menu(self)
        
        self.filemenu = tk.Menu(self)
        self.filemenu.add_command(label="New Window", command=self.new)
        self.filemenu.add_command(label="Save", command=self.savefile)
        self.filemenu.add_command(label="Save As", command=self.savefileas)
        self.filemenu.add_command(label="Open", command=self.openfile)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.config(menu=self.menubar)
    
    def savefile(self, *args, **kwargs):
        pass

    def savefileas(self, *args, **kwargs):
        pass

    def openfile(self, *args, **kwargs):
        pass

    def new(self, *args, **kwargs):
        pass

t = textpad()

t.mainloop()
