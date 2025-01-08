from tkinter import LabelFrame, Frame, Canvas, Label, Button, Entry, Toplevel

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

        self.delete_button = Button(self.file_button_frame, text="Delete")
        self.delete_button.grid(padx=5, pady=5, row=1, column=1, sticky='ns')
        self.create_button = Button(self.file_button_frame, text="Create")
        self.create_button.grid(padx=5, pady=5, row=1, column=2, sticky='ns')
        self.create_button = Button(self.file_button_frame, text="test", command=self.messageWindow)
        self.create_button.grid(padx=5, pady=5, row=2, column=1, sticky='ns')

    def set_selected(self, tag):
        self.selected_file = tag

    def set_viewer(self, folder_info):
        self.explorer_canvas.delete("all")
        x = 10
        y = 0
        index = 0
        for file in folder_info:
            txt = file + "\n"
            tag = file.replace(" ", "*-*")
            self.explorer_canvas.create_rectangle(0, y, 200, y + 30, tags=[tag, tag + "_rect_element"], fill="white", outline="white")
            self.explorer_canvas.create_text(x, y + 22.5, text=txt, anchor='w', tags=[tag, tag + "_text_element"])
            y += 30
            index += 1

    def turn_selected(self, tag, mode):
        rect = tag + "_rect_element"
        text = tag + "_text_element"
        if mode == "on":
            self.explorer_canvas.itemconfig(rect, fill="grey", outline="grey")
            self.explorer_canvas.itemconfig(text, fill="white")
        elif mode == "off":
            self.explorer_canvas.itemconfig(rect, fill="white", outline="white")
            self.explorer_canvas.itemconfig(text, fill="black")
    
    def messageWindow(self):
        win = Toplevel()
        win.title('Save Changes')
        win.geometry("300x100")

        Label(win, text="Do you want to save your changes?").pack(padx=10, pady=10, fill='x')
        Button(win, text='Save', command=win.destroy).pack(padx=10, pady=10, side='left')
        Button(win, text='Discard', command=win.destroy).pack(padx=10, pady=10, side='left')
        Button(win, text='Cancel', command=win.destroy).pack(padx=10, pady=10, side='left')

    def clicked_file(self, event):
        tag = ""
        f = self.explorer_canvas.gettags("current")
        if f:
            tag = f[0]

        if tag != "":
            if tag == self.selected_file:
                return
            ## ----------------- #
            if self.selected_file != "":
                ## --- NEED TO SAVE IT --- #
                # self.parent.save_file(tag)
                ## ----------------------- #
                self.turn_selected(self.selected_file, "off")
            self.selected_file = tag
            self.turn_selected(self.selected_file, "on")
            ## --- LOAD FILE --- #
            self.set_name(self.selected_file.replace("*-*", " "))
            self.parent.load_file(self.selected_file.replace("*-*", " "))

    def set_name(self, file_name):
        self.name_entry.delete(0,"end")
        self.name_entry.insert(0, file_name)

    def create_file(self):
        pass
    
    def delete_file(self):
        pass