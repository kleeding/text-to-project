from tkinter import LabelFrame, Frame, Text, Scrollbar, Button

class UserInput(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.made_changes = True

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

        self.build_button = Button(self.input_button_frame, text="Undo", width=10)
        self.build_button.pack(padx=10, pady=(10,5), ipady=7, side="left")
        self.build_button = Button(self.input_button_frame, text="Save", width=10, command=self.save_text)
        self.build_button.pack(padx=10, pady=(10,5), side="right", fill='y')

    def set_input(self, content):
        self.text_entry.delete(1.0,"end")
        for i in range(len(content)):
            self.text_entry.insert(str(i + 1) + ".0", content[i])

    def save_text(self):
        if self.made_changes:
            content = self.text_entry.get(1.0, 'end-1c')
            self.parent.save_file(content)