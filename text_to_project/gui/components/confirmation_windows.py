from tkinter import Toplevel, Label, Button

class ConfirmationWindow(Toplevel):
    def __init__(self, parent, title, geometry, message, buttons):
        super().__init__(parent)

        self.title(title)
        self.geometry(geometry)

        self.grid_rowconfigure(0, weight=1)
        self.rows = len(buttons)
        
        Label(self, text=message).grid(pady=(25,0), row=0, column=0, columnspan=self.rows, sticky="news")

        for i in range(self.rows):
            self.columnconfigure(i, weight=1, uniform=1)
            confirm_button = Button(self, text=buttons[i], width=8, command = lambda x=i: self.return_confirm(x))
            confirm_button.grid(padx=10, pady=15, row=1, column=i)

    def return_confirm(self, content):
        self.confirm = content
        self.destroy()

    def show(self):
        self.deiconify()
        self.wm_protocol("WM_DELETE_WINDOW", self.destroy)
        self.wait_window(self)
        return self.confirm