#!/usr/bin/env python3

""" Name that Shape module for use with Lab 5, Inf1340, Fall 2015 """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def name_that_shape(sides):
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs | Expected Outputs
    -------------------------
      < 3  | Error
      3    | triangle
      4    | quadrilateral
      5    | pentagon
      6    | hexagon
      7    | heptagon
      8    | octagon
      9    | nonagon
      10   | decagon
      > 10 | Error

    Errors: TypeError when input is a string or float
            ValueError when input is < 3 or > 10

    """

    if sides.isdigit() or sides[0] is "-" and sides[1:].isdigit():
        sides = int(sides)
    else:
        raise TypeError

    shape_name = ""

    if sides == 3:
        shape_name = "triangle"
    elif sides == 4:
        shape_name = "quadrilateral"
    elif sides == 5:
        shape_name = "pentagon"
    elif sides == 6:
        shape_name = "hexagon"
    elif sides == 7:
        shape_name = "heptagon"
    elif sides == 8:
        shape_name = "octagon"
    elif sides == 9:
        shape_name = "nonagon"
    elif sides == 10:
        shape_name = "decagon"
    else:
        raise ValueError

    return shape_name

#name_that_shape(6)