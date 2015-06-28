import Tkinter as tk
import tkFileDialog
from ScrolledText import ScrolledText

class textpad(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.st = ScrolledText()
        self.st.pack()

        self.fileloc = None
        
        self.menubar = tk.Menu(self)
        
        self.filemenu = tk.Menu(self)
        self.filemenu.add_command(label="New Window", command=self.new)
        self.filemenu.add_command(label="Save", command=self.savefile)
        self.filemenu.add_command(label="Save As", command=self.savefileas)
        self.filemenu.add_command(label="Open", command=self.openfile)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.config(menu=self.menubar)
    
    def savefile(self, *args, **kwargs):
        if self.fileloc:
            open(self.fileloc, 'w+').write(self.gettext())
        else:
            self.fileloc = self.getsavefname()
            open(self.fileloc, 'w+').write(self.gettext())

    def savefileas(self, *args, **kwargs):
        self.fileloc = self.getsavefname()
        open(self.fileloc, 'w+').write(self.gettext())

    def openfile(self, *args, **kwargs):
        self.settext(open(self.getopenfname()).read())

    def settext(self, text):
        self.cleartext
        self.st.insert('1.0', text)
    
    def cleartext(self):
        self.st.delete('1.0', 'end')

    def gettext(self):
        return self.st.get('1.0', 'end')
    
    def new(self, *args, **kwargs):
        pass

    def getsavefname(self):
        return tkFileDialog.asksaveasfilename()

    def getopenfname(self):
        return tkFileDialog.askopenfilename()

t = textpad()

t.mainloop()
