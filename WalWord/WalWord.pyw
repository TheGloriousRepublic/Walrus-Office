from Tkinter import *
from ScrolledText import ScrolledText

class WalWord(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.formatting = Frame(self)
        self.formatting.pack()
        
        self.bold = Button(self.formatting, text='B')
        self.bold.grid(row=0, column=0)

        self.italic = Button(self.formatting, text='I')
        self.italic.grid(row=0, column=1)

        self.underline = Button(self.formatting, text='U')
        self.underline.grid(row=0, column=2)
        
        self.strike = Button(self.formatting, text='S')
        self.strike.grid(row=0, column=3)
        
        self.st = ScrolledText()
        self.st.pack(fill=BOTH, expand=1)

ww = WalWord()

ww.mainloop()
