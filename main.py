from com.masolar.CustomWidgets import *
from tkColorChooser import askcolor


def get_color():
    color = askcolor(painter.line_color.get())

    if color[1]:
        painter.line_color.set(color[1])

root = Tk()
root.title("Mandala Painter")

"""
Setups the parameters of the Mandala Painter
"""
divisions_dialog = MandalaSetupDialog(root)

params = divisions_dialog.result

toolbar = Frame(root)
toolbar.pack(side=TOP)

painter = MandalaPainter(root, *params)


slider = Scale(toolbar, from_=1, to=30, orient=HORIZONTAL, var=painter.line_width)
slider.grid(row=0, column=1)
slider.set(10)

clear_button = Button(toolbar, text="Clear", command=painter.clear)
clear_button.grid(row=0, column=0)

color_button = Button(toolbar, text="Color", command=get_color)
color_button.grid(row=0, column=2)

root.mainloop()