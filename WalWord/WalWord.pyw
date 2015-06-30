from Tkinter import *
from ScrolledText import ScrolledText

class WalWord(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.formatting = Frame(self)
        self.formatting.pack(side=TOP, fill=X)

        self.font = StringVar()

        self.fontsize = OptionMenu(self.formatting, self.font, 5, 6, 8, 11, 12, 16, 20, 22, 26, 30)
        self.fontsize.grid(row=0, column=0)
        
        self.bold = Button(self.formatting, text='B', font=('Times', 10, 'bold'))
        self.bold.grid(row=0, column=1)

        self.italic = Button(self.formatting, text='I', font=('Times', 10, 'italic'))
        self.italic.grid(row=0, column=2)

        self.underline = Button(self.formatting, text='U', font=('Times', 10, 'underline'))
        self.underline.grid(row=0, column=3)
        
        self.strike = Button(self.formatting, text='S', font=('Times', 10, 'overstrike'))
        self.strike.grid(row=0, column=4)
        
        self.st = ScrolledText()
        self.st.pack(fill=BOTH, expand=1)

ww = WalWord()

ww.mainloop()
