from tkinter import LabelFrame, Text, Scrollbar

class TextEntry(LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(text="Text Editor")
        
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.text_entry = Text(self, width=15, wrap=None)
        self.text_entry.grid(padx=(5,0), pady=(5,0), row=0, column=0, sticky='news')

        self.x_scoller = Scrollbar(self, orient = 'horizontal', command = self.text_entry.xview)
        self.y_scoller = Scrollbar(self, orient = 'vertical', command = self.text_entry.yview)
        self.x_scoller.grid(row=1, column=0, sticky='we')
        self.y_scoller.grid(row=0, column=1, sticky='ns')
        
        self.text_entry['xscrollcommand'] = self.x_scoller.set   
        self.text_entry['yscrollcommand'] = self.y_scoller.set

