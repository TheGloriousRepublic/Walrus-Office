import Tkinter as tk
import tkMessageBox
import tkFileDialog
from ScrolledText import ScrolledText
import datetime

clipboard = ''
class textpad(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.st = ScrolledText()
        self.st.pack(fill=tk.BOTH, expand=1)

        self.fileloc = None
        
        self.menubar = tk.Menu(self, tearoff=False)
        
        self.filemenu = tk.Menu(self, tearoff=False)
        self.filemenu.add_command(label='New Window', command=self.new)
        self.filemenu.add_command(label='Save',       command=self.savefile)
        self.filemenu.add_command(label='Save As',    command=self.savefileas)
        self.filemenu.add_command(label='Open',       command=self.openfile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit',       command=self.exitprogram)
        self.menubar.add_cascade(label='File',        menu=self.filemenu)

        self.editmenu = tk.Menu(self, tearoff=False)
        self.editmenu.add_command(label='Undo',       command=self.undochange)
        self.editmenu.add_command(label='Redo',       command=self.redochange)
        self.editmenu.add_separator()
        self.editmenu.add_command(label='Cut',        command=self.cuttext)
        self.editmenu.add_command(label='Copy',       command=self.copytext)
        self.editmenu.add_command(label='Glue',       command=self.gluetext)
        self.editmenu.add_command(label='Paste',      command=self.pastetext)
        self.editmenu.add_separator()

        self.timemenu = tk.Menu(self.editmenu, tearoff=False)
        self.editmenu.add_command(label='Insert Timestamp', command=self.timestamp)

        self.editmenu.add_cascade(label='Date/Time',  menu=self.timemenu)
        self.menubar.add_cascade(label='Edit',        menu=self.editmenu)

        self.st.bind('<ButtonRelease-3>', self.rclick)
        self.st.bind('<Control-s>', self.savefile)
        self.st.bind('<Control-o>', self.openfile)
        self.st.bind('<Control-n>', self.new)
        self.st.bind('<Control-w>', self.exitprogram)
        #self.st.bind('<Control-d>', self.timestamp)

        self.config(menu=self.menubar)

        self.issaved = True #Whether or not the current file is saved
        
    def savefile(self, event):
        if self.fileloc:
            open(self.fileloc, 'w+').write(self.getcontent())
        else:
            self.fileloc = self.getsavefname()
            if self.fileloc:
                open(self.fileloc, 'w+').write(self.getcontent())

    def savefileas(self, event):
        self.fileloc = self.getsavefname()
        open(self.fileloc, 'w+').write(self.getcontent())

    def openfile(self, event):
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
    
    def new(self, event):
        pass

    def getsavefname(self):
        return tkFileDialog.asksaveasfilename()

    def getopenfname(self):
        return tkFileDialog.askopenfilename()

    def cuttext(self, event):
        global clipboard
        clipboard = self.getselected()
        self.st.delete('SEL_FIRST', 'SEL_LAST')

    def copytext(self, event):
        global clipboard
        clipboard = self.getselected()

    def pastetext(self, event):
        global clipboard
        self.st.insert('INSERT', clipboard)

    def gluetext(self, event):
        global clipboard
        clipboard += self.getselected()

    def pastetext(self, event):
        pass

    def rclick(self, event):
        self.editmenu.post(event.x_root, event.y_root)

    def exitprogram(self, event):
        if not self.issaved:
            tkMessageBox.alert('Save current document?')
        self.quit()

    def undochange(self, event):
        pass

    def redochange(self, event):
        pass

    def timestamp(self, event):
        self.st.insert(tk.END, str(datetime.datetime.now()))

t = textpad()

t.mainloop()
