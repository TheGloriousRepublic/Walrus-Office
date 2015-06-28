import Tkinter as tk
import tkFileDialog
from ScrolledText import ScrolledText

clipboard = ''
class textpad(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.st = ScrolledText()
        self.st.pack(fill=tk.BOTH, expand=1)

        self.fileloc = None
        
        self.menubar = tk.Menu(self)
        
        self.filemenu = tk.Menu(self)
        self.filemenu.add_command(label='New Window', command=self.new)
        self.filemenu.add_command(label='Save',       command=self.savefile)
        self.filemenu.add_command(label='Save As',    command=self.savefileas)
        self.filemenu.add_command(label='Open',       command=self.openfile)
        self.menubar.add_cascade(label='File',        menu=self.filemenu)

        self.editmenu = tk.Menu(self)
        self.editmenu.add_command(label='Undo',       command=self.undochange)
        self.editmenu.add_command(label='Redo',       command=self.redochange)
        self.editmenu.add_command(label='Cut',        command=self.cuttext)
        self.editmenu.add_command(label='Copy',       command=self.copytext)
        self.editmenu.add_command(label='Glue',       command=self.gluetext)
        self.editmenu.add_command(label='Paste',      command=self.pastetext)
        self.menubar.add_cascade(label='Edit',        menu=self.editmenu)

        self.st.bind('<ButtonRelease-3>', self.rclick)

        self.bind('<ButtonRelease-1>', self.update)

        self.config(menu=self.menubar)

    def update(self, *args):
        print('Update!')
        self.st.update()
        
        
    def savefile(self, *args, **kwargs):
        if self.fileloc:
            open(self.fileloc, 'w+').write(self.getcontent())
        else:
            self.fileloc = self.getsavefname()
            open(self.fileloc, 'w+').write(self.getcontent())

    def savefileas(self, *args, **kwargs):
        self.fileloc = self.getsavefname()
        open(self.fileloc, 'w+').write(self.getcontent())

    def openfile(self, *args, **kwargs):
        self.settext(open(self.getopenfname()).read())

    def settext(self, text):
        self.cleartext
        self.st.insert('1.0', text)
    
    def cleartext(self):
        self.st.delete('1.0', 'end')

    def getcontent(self):
        return self.st.get('1.0', 'end')

    def getselected(self):
        return self.st.get('SEL_FIRST', 'SEL_LAST')
    
    def new(self, *args, **kwargs):
        pass

    def getsavefname(self):
        return tkFileDialog.asksaveasfilename()

    def getopenfname(self):
        return tkFileDialog.askopenfilename()

    def cuttext(self, *args):
        global clipboard
        clipboard = self.getselected()
        self.st.delete('SEL_FIRST', 'SEL_LAST')

    def copytext(self, *args):
        global clipboard
        clipboard = self.getselected()

    def pastetext(self, *args):
        global clipboard
        self.st.insert('INSERT', clipboard)

    def gluetext(self, *args):
        global clipboard
        clipboard += self.getselected()

    def pastetext(self, *args):
        pass

    def rclick(self, event):
        self.editmenu.post(event.x_root, event.y_root)

    def exitprogram(self):
        self.exit()

    def undochange(self, *args):
        pass

    def redochange(self, *args):
        pass

t = textpad()

t.mainloop()
