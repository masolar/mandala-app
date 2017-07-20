from Tkinter import *
from Converter import Radians
import math

class MandalaPainter:

    def __init__(self, master):

        self.width = 800
        self.height = 600

        self.x_shift = self.width // 2
        self.y_shift = self.height // 2

        self.canvas = Canvas(master, width=self.width, height=self.height)
        self.canvas.pack()
        self.canvas.bind("<B1-Motion>", self.mouse_down)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_up)

        self.old_motion_x = None
        self.old_motion_y = None

        self.divisions = 6

        self.create_grid()

    def mouse_down(self, event):

        if self.old_motion_x is not None:
            line = (self.old_motion_x, self.old_motion_y, event.x, event.y)
            self.canvas.create_line(*line)

            line = Radians.rotate_line(line, math.pi, (self.x_shift, self.y_shift))

            point_1 = Radians.rad_to_cart(line[0], line[1], (self.x_shift, self.y_shift))
            point_2 = Radians.rad_to_cart(line[2], line[3], (self.x_shift, self.y_shift))

            self.canvas.create_line(point_1, point_2)

        self.old_motion_x = event.x
        self.old_motion_y = event.y

    def mouse_up(self, event):
        self.old_motion_x = None
        self.old_motion_y = None

    def create_grid(self):
        pass

    def draw_polar(self, line):
        line_1 = [line[0], line[1]]
        line_2 = [line[2], line[3]]



if __name__ == '__main__':
    root = Tk()
    root.title("Mandala Painter")
    painter = MandalaPainter(root)
    root.mainloop()