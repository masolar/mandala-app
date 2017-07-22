from com.masolar.CustomWidgets import *
from tkColorChooser import askcolor


def get_color():
    color = askcolor(painter.line_color.get())

    if color[1]:
        painter.line_color.set(color[1])


def get_background_color():
    color = askcolor()

    if color[1]:
        painter.change_background(color[1])


def open_new_image():
    global painter

    divisions_dialog = MandalaSetupDialog(root)

    params = divisions_dialog.result

    if not params:
        if not painter:
            sys.exit()
        return

    if painter:
        painter.canvas.destroy()

    painter = MandalaPainter(root, *params)
    setup_ui()


def setup_ui():
    global toolbar

    if toolbar:
        toolbar.destroy()

    toolbar = Frame(root)
    toolbar.pack(side=TOP)

    new_button = Button(toolbar, text="New", command=open_new_image)
    new_button.grid(row=0, column=0)

    slider = Scale(toolbar, from_=1, to=30, orient=HORIZONTAL, var=painter.line_width)
    slider.grid(row=0, column=2)
    slider.set(10)

    clear_button = Button(toolbar, text="Clear", command=painter.clear)
    clear_button.grid(row=0, column=1)

    color_button = Button(toolbar, text="Color", command=get_color)
    color_button.grid(row=0, column=3)

    color_background_button = Button(toolbar, text="Background", command=get_background_color)
    color_background_button.grid(row=0, column=4)


root = Tk()
root.title("Mandala Painter")

# Set it to None at first so we can call the open_new_image function
painter = None
toolbar = None

"""
Setups the parameters of the Mandala Painter App
"""
open_new_image()

root.mainloop()