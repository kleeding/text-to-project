from tkinter import LabelFrame, Frame, Text

class ProjectViewer(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.diagram_frame = LabelFrame(self, text="Diagram Viewer")
        self.diagram_frame.pack(padx=5, pady=5, fill='both', expand=True)

        # self.diagram_canvas = Canvas(self.diagram_frame, bg="white")
        # self.diagram_canvas.pack(padx=5, pady=5, fill="both", expand=True)

        self.text_entry = Text(self.diagram_frame, width=15, wrap=None)
        self.text_entry.pack(padx=5, pady=5, fill="both", expand=True)

    def set_content(self, content):
        self.text_entry.delete(1.0, "end")
        for i in range(len(content)):
            self.text_entry.insert(str(i + 1) + ".0", content[i])
        self.content = self.get_input()

    def get_input(self):
        content = self.text_entry.get(1.0, 'end-1c')
        return content