from tkinter import LabelFrame, Frame, Text, Button

class TextEditor(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # self.config(bg="green")

        self.text_editor_frame = LabelFrame(self, text="Text Editor")
        self.text_editor_frame.pack(fill="both", expand=True)

        self.text_entry = Text(self.text_editor_frame, wrap = "none")
        self.text_entry.pack(padx=5, pady=5, fill="both", expand=True)

        self.button_frame = Frame(self)
        self.button_frame.pack(fill="both")

        self.build_button = Button(self.button_frame, text="Build\nProject", width=10)
        self.build_button.pack(padx=10, pady=(10,5), side="right")
        self.create_diagram_button = Button(self.button_frame, text="Create\nDiagram", width=10)
        self.create_diagram_button.pack(padx=10, pady=(10,5), side="right")

