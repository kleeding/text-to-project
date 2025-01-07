from tkinter import Frame, Entry, Label, Button
from gui.components.file_viewer import FileViewer

class FileExplorer(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # For this: need to create backend script that grabs all folders/text files in project folder
        # this info needs to be passed to this class

        ## Add folders in future
        # dummy data
        self.folder_info = ["Shopping Cart", "Payment System", "Calculator", "QR Generator", "Random Image"]
        
        self.file_viewer = FileViewer(self, self.folder_info)
        self.file_viewer.pack(fill="both", expand=True)

        # --- Set up Buttons --- #
        self.button_frame = Frame(self)
        self.button_frame.pack()

        self.name_label = Label(self.button_frame, text="Name:")
        self.name_label.grid(padx=5, pady=5, row=0, column=0)

        self.name_entry = Entry(self.button_frame)
        self.name_entry.grid(padx=5, pady=5, row=0, column=1, columnspan=2, sticky='news')

        self.delete_button = Button(self.button_frame, text="Delete", command=self.delete_file)
        self.delete_button.grid(padx=5, pady=5, row=1, column=1, sticky='ns')
        self.create_button = Button(self.button_frame, text="Create", command=self.create_file)
        self.create_button.grid(padx=5, pady=5, row=1, column=2, sticky='ns')

    def set_name(self, file_name):
        self.name_entry.delete(0,"end")
        self.name_entry.insert(0, file_name)

    def load_file(self, file_name):
        print(file_name)
        ## --- LOAD FILE FROM PROJECT FOLDER WITH NAME FILE_NAME
        ## --- DELETE THEN INSERT INTO TEXT EDITOR WIDGET
        return

    def create_file(self):
        file_name = self.name_entry.get()
        if file_name != "" and file_name not in self.folder_info:
            ## CREATE TEXT FILE IN PROJECT FOLDER
            self.folder_info.append(file_name)
            self.file_viewer.set_viewer(sorted(self.folder_info)) # Add to file explorer
        
    ## --- ADD A CONFIRM MESSAGE FOR DELETION --- #
    def delete_file(self):
        file_name = self.name_entry.get()
        if file_name != "" and file_name in self.folder_info:
            print(True)
            # DELETE FILE FROM PROJECT FOLDER
            self.folder_info.remove(file_name)
            self.file_viewer.set_viewer(sorted(self.folder_info)) # Add to file explorer