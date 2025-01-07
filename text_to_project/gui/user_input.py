from tkinter import Frame, Button
from gui.components.text_entry import TextEntry

class UserInput(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # --- Set up Text Editor --- #
        self.text_entry = TextEntry(self)
        self.text_entry.pack(fill='both', expand=True)

        # --- Set up Buttons --- #
        self.button_frame = Frame(self)
        self.button_frame.pack(fill="both")

        self.build_button = Button(self.button_frame, text="Build\nProject", width=10)
        self.build_button.pack(padx=10, pady=(10,5), side="right")
        self.create_diagram_button = Button(self.button_frame, text="Create\nDiagram", width=10)
        self.create_diagram_button.pack(padx=10, pady=(10,5), side="right")
        self.build_button = Button(self.button_frame, text="Save", width=10)
        self.build_button.pack(padx=10, pady=(10,5), side="right", fill='y')

    def set_text(self):
        return  
    
    def get_text(self):
        return

    def save_text(self):
        return