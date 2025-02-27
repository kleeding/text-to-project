from tkinter import LabelFrame, Frame, Canvas, Label, Button, Entry
from gui.components.confirmation_windows import ConfirmationWindow

class FileExplorer(LabelFrame):
    def __init__(self, parent, file_names):
        super().__init__(parent)
        self['text'] = "File Explorer"
        self.parent = parent
        self.file_names = file_names ## Add functionality for folders in future ##
        self.selected_file = ""

        # --- Set up file viewer --- #
        self.explorer_canvas = Canvas(self, width=120, bg='white')
        self.explorer_canvas.pack(padx=5, pady=5, fill='both', expand=True)
        self.explorer_canvas.bind("<Button-1>", self.clicked_file)
        self.set_viewer(self.file_names)

        self.file_button_frame = Frame(self)
        self.file_button_frame.pack()

        self.name_label = Label(self.file_button_frame, text="Name:")
        self.name_label.grid(padx=5, pady=5, row=0, column=0)

        self.name_entry = Entry(self.file_button_frame)
        self.name_entry.grid(padx=5, pady=5, row=0, column=1, columnspan=2, sticky='news')

        self.delete_button = Button(self.file_button_frame, text="Delete", command=self.delete_file)
        self.delete_button.grid(padx=5, pady=5, row=1, column=1, sticky='ns')
        self.create_button = Button(self.file_button_frame, text="Create", command=self.create_file)
        self.create_button.grid(padx=5, pady=5, row=1, column=2, sticky='ns')

    def set_selected(self, tag):
        self.selected_file = tag

    def set_viewer(self, folder_info):
        self.explorer_canvas.delete("all")
        s = 25
        x = 10
        y = 0
        index = 0
        for file in folder_info:
            txt = file + "\n"
            tag = file.replace(" ", "*-*")
            self.explorer_canvas.create_rectangle(0, y, 200, y + s, tags=[tag, tag + "_rect_element"], fill="white", outline="white")
            self.explorer_canvas.create_text(x, y + (s / 2 + 8), text=txt, anchor='w', tags=[tag, tag + "_text_element"])
            y += s
            index += 1
        self.selected_file = ""

    def turn_selected(self, tag, mode):
        rect = tag + "_rect_element"
        text = tag + "_text_element"
        if mode == "on":
            self.explorer_canvas.itemconfig(rect, fill="grey", outline="grey")
            self.explorer_canvas.itemconfig(text, fill="white")
        elif mode == "off":
            self.explorer_canvas.itemconfig(rect, fill="white", outline="white")
            self.explorer_canvas.itemconfig(text, fill="black")

    def clicked_file(self, event):
        tag = ""
        tags = self.explorer_canvas.gettags("current")
        if tags:
            tag = tags[0]
        if tag != "":
            if tag == self.selected_file: # <-- Same file clicked - do nothing
                return
            if self.selected_file != "": # <-- Indicating changing files
                if self.parent.changes_made(): # <-- if changes have been made, see if these should be saved
                    confirmation = ConfirmationWindow(self, 
                                                      "Save Changes", 
                                                      "300x100", 
                                                      "Do you want to save your changes?",
                                                      ["Save", "Discard", "Cancel"])
                    confirm = confirmation.show()
                    print(confirm)
                    if confirm == 2:
                        return # < -- Cancelled
                    elif confirm == 0:
                        self.parent.save_file()
                self.turn_selected(self.selected_file, "off")
            self.selected_file = tag
            self.turn_selected(self.selected_file, "on")
            ## --- LOAD FILE --- #
            file_name = self.selected_file.replace("*-*", " ")
            self.set_name(file_name)
            self.parent.load_file()

    def set_name(self, file_name):
        self.name_entry.delete(0,"end")
        self.name_entry.insert(0, file_name)

    def get_name_selected(self):
        file_name = self.selected_file.replace("*-*", " ")
        return file_name
    
    # def get_name_input(self):
    #     file_name = self.name_entry.get()
    #     return file_name

    def create_file(self):
        file_name = self.name_entry.get()
        if file_name != "":
                self.parent.create_file(file_name)
    
    def delete_file(self):
        file_name = self.get_name_selected()
        if file_name != "":
            self.parent.delete_file(file_name)