from tkinter import LabelFrame, Canvas

class DiagramViewer(LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg="blue")
        self.config(text="DiagramViewer")

        self.diagram_canvas = Canvas(self, bg="white")
        self.diagram_canvas.pack(padx=5, pady=5, fill="both", expand=True)