import math

"""
Small file to perform cart and polar conversions
"""

"""
Asks for a shift in case the origin is not the top left corner of the widget
"""
def cart_to_rad(x, y, origin = (0, 0)):
    shifted_x = x - origin[0]

    # Y is opposite because the coordinates have y increasing the lower in the widget you go.
    shifted_y = origin[1] - y

    return (distance(shifted_x, shifted_y), math.atan2(shifted_y, shifted_x))

def distance(x, y):
    return math.sqrt(x ** 2 + y ** 2)

def rad_to_cart(r, theta, origin = (0, 0)):
    return (int(r * math.cos(theta) + origin[0]), int(origin[1] + -(r * math.sin(theta))))

def rotate_line(x_1, y_1, x_2, y_2, rot_amount, origin = (0, 0)):
    end_1 = cart_to_rad(x_1, y_1, origin)
    end_2 = cart_to_rad(x_2, y_2, origin)

    return (end_1[0], end_1[1] + rot_amount, end_2[0], end_2[1] + rot_amount)

def rotate_line(line, rot_amount, origin = (0, 0)):
    x_1 = line[0]
    y_1 = line[1]
    x_2 = line[2]
    y_2 = line[3]

    end_1 = cart_to_rad(x_1, y_1, origin)
    end_2 = cart_to_rad(x_2, y_2, origin)

    return (end_1[0], end_1[1] + rot_amount, end_2[0], end_2[1] + rot_amount)