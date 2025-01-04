from tkinter import LabelFrame, Canvas

class FileExplorer(LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        # self.config(bg="red")
        self.config(text="File Explorer")

        self.text = Canvas(self, width=150, bg="white")
        self.text.pack(padx=5, pady=5, fill="both", expand=True)