import Tkinter as tk
from ScrolledText import ScrolledText

class textpad(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.st = ScrolledText()
        self.st.pack()

        menubar = tk.Menu(self)
        menubar.add_command(label="Hello!")

        self.config(menu=menubar)

t = textpad()

t.mainloop()
