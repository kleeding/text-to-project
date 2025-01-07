from tkinter import LabelFrame, Text, Canvas

class FileViewer(LabelFrame):
    def __init__(self, parent, folder_info):
        super().__init__(parent)
        self["text"] = "File Explorer"
        self.parent = parent

        self.selected_file = ""

        self.explorer_canvas = Canvas(self, width=120, bg='white')
        self.explorer_canvas.pack(padx=5, pady=5, fill='both', expand=True)

        self.set_viewer(sorted(folder_info))

        self.explorer_canvas.bind("<Button-1>", self.clicked_file)

    color = ['white', 'green', 'red', 'blue']

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
    
    def clicked_file(self, event):
        tag = ""
        f = self.explorer_canvas.gettags("current")
        if f:
            tag = f[0]
        if tag != "":
            if tag != self.selected_file:
                self.turn_selected(tag, "on")
                ## --- LOAD FILE --- #
                self.parent.set_name(tag.replace("*-*", " "))
                self.parent.load_file(tag.replace("*-*", " "))

                ## ----------------- #
                if self.selected_file != "":
                    self.turn_selected(self.selected_file, "off")
                self.selected_file = tag