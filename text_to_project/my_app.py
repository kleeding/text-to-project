from tkinter import Tk, Frame
from gui.file_explorer import FileExplorer
from gui.user_input import UserInput
from gui.diagram_viewer import DiagramViewer

class MainWindow(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.columnconfigure((1,2), weight=1, uniform=True)
        self.rowconfigure(0, weight=1)

        # Create file explorer
        self.file_explorer = FileExplorer(self)
        self.file_explorer.grid(padx=5, pady=5, row=0, column=0, sticky="news")

        # Create text editor
        self.user_input = UserInput(self)
        self.user_input.grid(padx=5, pady=5, row=0, column=1, sticky="news")

        # Create diagram viewer
        self.diagram_viewer = DiagramViewer(self)
        self.diagram_viewer.grid(padx=5, pady=5, row=0, column=2, sticky="news")

if __name__ == "__main__":
    # Sort out folder/file information
    # folder_info = holds a list of (folder_name, (file1, ..., fil2n)) tuples
    
    # Create the root window
    root = Tk()
    root.title("Text to Project")
    root.geometry("1400x800")
    root.minsize(width=800, height=500)
 
    # Create the application
    app = MainWindow(root)
    app.pack(fill="both", expand=True)

    root.mainloop()