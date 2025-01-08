from tkinter import Tk, Frame
from gui.file_explorer import FileExplorer
from gui.user_input import UserInput
from gui.diagram_viewer import DiagramViewer
from gui.backend.file_manager import FileManager

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
        self.diagram_viewer = DiagramViewer(self)
        self.diagram_viewer.grid(padx=5, pady=5, row=0, column=2, sticky="news")

    def load_file(self, file_name):
        if file_name != "":
            file_contents = self.file_manager.load_file(file_name + ".txt")
        else:
            file_contents = ""
        self.user_input.set_input(file_contents)

    def save_file(self):
        if self.user_input.made_changes:
            content = self.user_input.get_text()
            print("Need to save")

    def create_file(self):
        pass
        # file_name = self.name_entry.get()
        # if file_name != "" and file_name not in self.file_names:
        #     self.parent.file_manager.create_file(file_name)
        #     self.file_names = self.parent.file_manager.get_names()
        #     self.file_viewer.set_viewer(self.file_names)
        #     self.parent.load_file(file_name)
        #     tag = file_name.replace(" ", "*-*")
        #     self.file_viewer.set_selected(tag)
        #     self.file_viewer.turn_selected(tag, "on")
        
    ## --- ADD A CONFIRM MESSAGE FOR DELETION --- #
    def delete_file(self):
        pass
        # file_name = self.name_entry.get()
        # if file_name != "" and file_name in self.file_names:
        #     # DELETE FILE FROM PROJECT FOLDER
        #     self.parent.file_manager.delete_file(file_name)
        #     self.file_names = self.parent.file_manager.get_names()
        #     self.file_viewer.set_viewer(self.file_names)
        #     self.parent.load_file("")

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