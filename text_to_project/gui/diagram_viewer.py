from tkinter import LabelFrame, Frame, Canvas, Button

class DiagramViewer(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.diagram_frame = LabelFrame(self, text="Diagram Viewer")
        self.diagram_frame.pack(padx=5, pady=5, fill='both', expand=True)

        self.diagram_canvas = Canvas(self.diagram_frame, bg="white")
        self.diagram_canvas.pack(padx=5, pady=5, fill="both", expand=True)

        # --- Set up Diagram Buttons --- #
        self.diagram_button_frame = Frame(self)
        self.diagram_button_frame.pack()

        self.create_diagram_button = Button(self.diagram_button_frame, text="Create\nDiagram", width=10)
        self.create_diagram_button.pack(padx=10, pady=(10,5), side="left")
        self.build_button = Button(self.diagram_button_frame, text="Build\nProject", width=10)
        self.build_button.pack(padx=10, pady=(10,5), side="left")