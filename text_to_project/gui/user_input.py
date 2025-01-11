from tkinter import LabelFrame, Frame, Text, Label, Scrollbar, Button, Toplevel

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
        self.build_button.pack(padx=10, pady=(10,5), side="right", fill='y')

    def set_content(self, content):
        self.text_entry.delete(1.0,"end")
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
            print(self.content)
            self.content = self.get_input()
            print(self.content)

    def undo_changes(self):
        made_changes = self.has_changed()
        if made_changes:
            confirmation = ConfirmationUndoWindow(self)
            confirm = confirmation.show()
            if confirm:
                self.parent.load_file()

class ConfirmationUndoWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title('Undo Changes')
        self.geometry("300x100")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0,1), weight=1, uniform=1)

        self.confirmation_return = False
        
        Label(self, text="Are you sure you want to undo your changes?").grid(pady=(25,0), row=0, column=0, columnspan=2, sticky="news")
        Button(self, text='Undo', width=8, command=self.undo).grid(padx=(10), pady=15, row=1, column=0, sticky="e")
        Button(self, text='Cancel', width=8, command=self.destroy).grid(padx=10, pady=15, row=1, column=1, sticky="w")

    def undo(self):
        self.confirmation_return = True
        self.destroy()

    def show(self):
        self.deiconify()
        self.wm_protocol("WM_DELETE_WINDOW", self.destroy)
        self.wait_window(self)
        return self.confirmation_return