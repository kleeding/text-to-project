from tkinter import LabelFrame, Frame, Text, Label, Scrollbar, Button
from gui.components.confirmation_windows import ConfirmationWindow
class UserInput(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # --- Set up Text Editor --- #
        self.editor_frame = LabelFrame(self, text="Text Editor")
        self.editor_frame.pack(padx=5, pady=5, fill='both', expand=True)        
        self.editor_frame.rowconfigure(0, weight=1)
        self.editor_frame.columnconfigure(0, weight=1)

        self.text_entry = Text(self.editor_frame, width=15, wrap=None)
        self.text_entry.grid(padx=(5,0), pady=(5,0), row=0, column=0, sticky='news')

        self.x_scoller = Scrollbar(self.editor_frame, orient = 'horizontal', command = self.text_entry.xview)
        self.y_scoller = Scrollbar(self.editor_frame, orient = 'vertical', command = self.text_entry.yview)
        self.x_scoller.grid(row=1, column=0, sticky='we')
        self.y_scoller.grid(row=0, column=1, sticky='ns')
        
        self.text_entry['xscrollcommand'] = self.x_scoller.set   
        self.text_entry['yscrollcommand'] = self.y_scoller.set
        
        # --- Set up Editor Buttons --- #
        self.input_button_frame = Frame(self)
        self.input_button_frame.pack()

        self.build_button = Button(self.input_button_frame, text="Undo", width=10, command=self.undo_changes)
        self.build_button.pack(padx=10, pady=(10,5), ipady=7, side="left")
        self.build_button = Button(self.input_button_frame, text="Save", width=10, command=self.save_text)
        self.build_button.pack(padx=10, pady=(10,5), side="left", fill='y')
        self.create_diagram_button = Button(self.input_button_frame, text="Create\nDiagram", width=10)
        self.create_diagram_button.pack(padx=10, pady=(10,5), side="left")
        self.build_button = Button(self.input_button_frame, text="Build\nProject", width=10, command=self.build_project)
        self.build_button.pack(padx=10, pady=(10,5), side="left")

    def build_project(self):
        self.parent.build_project()

    def set_content(self, content):
        self.text_entry.delete(1.0, "end")
        for i in range(len(content)):
            self.text_entry.insert(str(i + 1) + ".0", content[i])
        self.content = self.get_input()

    def has_changed(self):
        input = self.get_input()
        if self.content == input:
            return False
        return True

    def get_input(self):
        content = self.text_entry.get(1.0, 'end-1c')
        return content

    def save_text(self):
        made_changes = self.has_changed()
        if made_changes:
            self.parent.save_file()
            self.content = self.get_input()

    def undo_changes(self):
        made_changes = self.has_changed()
        if made_changes:
            confirmation = ConfirmationWindow(self, 
                                              "Undo Changes", 
                                              "300x100",
                                              "Are you sure you want to undo your changes?",
                                              ["Undo", "Cancel"])
            confirm = confirmation.show()
            if confirm == 0: # <-- Confirmed to undo text
                self.parent.load_file()