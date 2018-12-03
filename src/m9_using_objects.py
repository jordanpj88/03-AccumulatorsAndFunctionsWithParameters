"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Parker Jordan.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()

def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # Done: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------
    window = rg.RoseWindow(400, 400)
    center1 = rg.Point(200, 200)
    center2 = rg.Point(350, 100)
    circle1 = rg.Circle(center1,30)
    circle1.fill_color = 'midnight blue'
    circle2 = rg.Circle(center2, 50)
    circle1.attach_to(window)
    circle2.attach_to(window)
    window.render()

    window.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # Done: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------
    window = rg.RoseWindow(400, 400)
    x_1 = 200
    y_1 = 200
    center1 = rg.Point(x_1, y_1)
    color1 = 'blue'
    pen_thickness1 = 3
    circle = rg.Circle(center1, 50)
    circle.pen = rg.Pen('red', pen_thickness1)
    circle.fill_color = color1
    circle.attach_to(window)

    x_2 = 50
    y_2 = 25
    center2 = rg.Point(x_2, y_2)
    color2 = 'None'
    pen_thickness2 = 1
    rectangle = rg.Rectangle(rg.Point(250, 100), rg.Point(150, 50))
    rectangle.attach_to(window)
    rectangle.attach_to(window)

    window.render()
    window.close_on_mouse_click()

    print(pen_thickness1)
    print(color1)
    print(center1)
    print(x_1)
    print(y_1)

    print(pen_thickness2)
    print(color2)
    print(center2)
    print(x_2)
    print(y_2)



def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # Done: 4. Implement and test this function.
    window = rg.RoseWindow(400, 400)
    line1 = rg.Line(rg.Point(100, 100), rg.Point(200, 200))

    line2 = rg.Line(rg.Point(300, 300), rg.Point(350, 350))
    line2.thickness = 5
    center = line2.get_midpoint()

    print()
    print(center)
    print(325.0)
    print(325.0)

    line1.attach_to(window)
    line2.attach_to(window)
    window.render()
    window.close_on_mouse_click()

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
