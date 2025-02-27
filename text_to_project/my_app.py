from tkinter import Tk, Frame
from gui.file_explorer import FileExplorer
from gui.user_input import UserInput
from gui.project_viewer import ProjectViewer
from gui.components.confirmation_windows import ConfirmationWindow
from gui.backend.file_manager import FileManager
from gui.backend.project_parser import project_parser

class WindowManager(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.file_manager = FileManager(project_path)

        self.columnconfigure((1,2), weight=1, uniform=True)
        self.rowconfigure(0, weight=1)

        # Create file explorer
        self.file_explorer = FileExplorer(self, self.file_manager.get_names())
        self.file_explorer.grid(padx=5, pady=5, row=0, column=0, sticky="news")

        # Create text editor
        self.user_input = UserInput(self)
        self.user_input.grid(padx=5, pady=5, row=0, column=1, sticky="news")

        # Create diagram viewer
        self.project_viewer = ProjectViewer(self)
        self.project_viewer.grid(padx=5, pady=5, row=0, column=2, sticky="news")

    def load_file(self):
        file_name = self.file_explorer.get_name_selected()
        if file_name != "": 
            file_contents = self.file_manager.load_file(file_name + ".txt")
        else:
            file_contents = ['']
        self.user_input.set_content(file_contents)

    def save_file(self):
            file_name = self.file_explorer.get_name_selected()
            content = self.user_input.get_input()
            self.file_manager.save_file(file_name, content)

    def create_file(self, file_name):
        current_files = self.file_manager.get_names()
        if file_name not in current_files: # <-- file doesn't exist
            self.file_manager.create_file(file_name) # create it
            file_names = self.file_manager.get_names()
            self.file_explorer.set_viewer(file_names)
            tag = file_name.replace(" ", "*-*")
            self.file_explorer.set_selected(tag)
            self.file_explorer.turn_selected(tag, "on")
            self.load_file()
        
    def delete_file(self, file_name):
        current_files = self.file_manager.get_names()
        if file_name in current_files:
            confirmation = ConfirmationWindow(self,
                                              "Confirm Delete",
                                              "300x100",
                                              "Are you sure you want to delete this file?",
                                              ["Yes", "Cancel"])
            confirmed = confirmation.show()
            if confirmed == 1: # <-- user cancelled deletion
                return
            self.file_manager.delete_file(file_name)
            file_names = self.file_manager.get_names()
            self.file_explorer.set_viewer(file_names)
            self.load_file()

    def changes_made(self):
        output = self.user_input.has_changed()
        return output

    def build_project(self):
        content = self.user_input.get_input()
        if content != "":
            project = project_parser(content)
        if project:
            self.project_viewer.set_content(project)

if __name__ == "__main__":    
    project_path = "text_to_project\projects"

    # Create the root window
    root = Tk()
    root.title("Text to Project")
    root.geometry("1400x800")
    root.minsize(width=800, height=500)
 
    # Create the application
    app = WindowManager(root)
    app.pack(fill="both", expand=True)

    root.mainloop()