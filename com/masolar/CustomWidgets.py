from Tkinter import *
from Converter import Radians
import math

"""
This class represents a widget which allows the user to draw mandalas around the central part
of the canvas.
"""
class MandalaPainter:
    def __init__(self, master, width, height, divisions):
        self.width = width
        self.height = height

        self.origin_x = self.width // 2
        self.origin_y = self.height // 2

        self.canvas = Canvas(master, width=self.width, height=self.height)
        self.canvas.pack(side=BOTTOM)
        self.canvas.bind("<B1-Motion>", self.mouse_down)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_up)

        self.old_motion_x = None
        self.old_motion_y = None

        self.line_width = IntVar()
        self.line_color = StringVar()
        self.line_color.set('#000000')

        # Represents the number of sections the canvas is divided into
        self.divisions = divisions

        # Holds the angles for each section of the canvas
        self.angles = []

        for i in range(0, self.divisions):
            self.angles.append((i * 2 * math.pi) / self.divisions)

        self.create_grid()

    def mouse_down(self, event):
        if self.old_motion_x is not None:
            line = (self.old_motion_x, self.old_motion_y, event.x, event.y)
            self.canvas.create_line(*line, fill=self.line_color.get(), width=self.line_width.get(), capstyle=ROUND, smooth=1)

            # For each other line, rotate it around the origin, then redraw it at the new orientation
            for i in range(1, self.divisions):
                new_line = Radians.rotate_line(line, self.angles[i], (self.origin_x, self.origin_y))

                point_1 = Radians.polar_to_cart(new_line[0], new_line[1], (self.origin_x, self.origin_y))
                point_2 = Radians.polar_to_cart(new_line[2], new_line[3], (self.origin_x, self.origin_y))

                self.canvas.create_line(point_1, point_2, fill=self.line_color.get(), width=self.line_width.get(), capstyle=ROUND, smooth=1)

        self.canvas.update_idletasks()

        self.old_motion_x = event.x
        self.old_motion_y = event.y

    def mouse_up(self, event):
        self.old_motion_x = None
        self.old_motion_y = None

    def clear(self):
        self.canvas.delete("all")
        self.create_grid()

    def change_background(self, new_color):
        self.canvas.configure(bg=new_color)
        self.canvas.update()

    def create_grid(self):
        line = self.origin_x, self.origin_y, 4 * self.origin_x, self.origin_y

        self.canvas.create_line(line, fill="black", width=1, capstyle=ROUND)

        for i in range(1, self.divisions):
            new_line = Radians.rotate_line(line, self.angles[i], (self.origin_x, self.origin_y))

            point_1 = Radians.polar_to_cart(new_line[0], new_line[1], (self.origin_x, self.origin_y))
            point_2 = Radians.polar_to_cart(new_line[2], new_line[3], (self.origin_x, self.origin_y))

            self.canvas.create_line(point_1, point_2, fill="black", width=1,
                                    capstyle=ROUND, smooth=1)


"""
This class defines the dialog that sets up the Mandala Painter.
"""
class MandalaSetupDialog(Toplevel):
    def __init__(self, parent, title=None):
        Toplevel.__init__(self, parent)
        self.transient(parent)

        if title:
            self.title(title)

        self.parent = parent

        self.result = None

        self.bind("<Return>", self.validate)

        self.grab_set()

        self.width_label = Label(self, text="Enter the width of the canvas")
        self.width_label.grid(row=0, column=0)
        self.width_input = Entry(self)
        self.width_input.grid(row=0, column=1)

        self.width_input.focus_set()

        self.height_label = Label(self, text="Enter the height of the canvas")
        self.height_label.grid(row=1, column=0)
        self.height_input = Entry(self)
        self.height_input.grid(row=1, column=1)

        self.divisions_label = Label(self, text="Enter the number of divisions")
        self.divisions_label.grid(row=2, column=0)
        self.divisions_input = Entry(self)
        self.divisions_input.grid(row=2, column=1)

        self.ok_button = Button(self, text="Ok", command=self.validate)
        self.ok_button.grid(row=3, column=1)

        self.error_message = StringVar()
        error_label = Label(self, textvariable=self.error_message)
        error_label.grid(row=4, column=0)

        self.wait_window(self)

    def validate(self, event=None):
        try:
            width = int(self.width_input.get())
            height = int(self.height_input.get())
            divisions = int(self.divisions_input.get())

            if width < 0 or height < 0 or divisions < 1:
                raise ValueError
        except ValueError:
            self.error_message.set("Please enter valid positive integers")
        else:
            self.result = width, height, divisions
            self.destroy()
