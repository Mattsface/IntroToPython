#!/usr/bin/env python
"""
keyword arguments:

Write a function that has four optional parameters (with defaults):
fore_color
back_color
link_color
visited_color
Have it print the colors (use strings for the colors)
Call it with a couple different parameters set
Have it pull the parameters out with *args, **kwargs
"""


def main():
    print colors()
    print colors(back_color="purple")
    first_two = ("green", "black")
    second_two = { 'link_color': 'orange', 'visited_color': 'blue' }
    print colors(*first_two, **second_two)

def colors(fore_color="black", back_color="red", link_color="green", visited_color="yellow"):
    return "The colors are %s, %s, %s, and %s" % (fore_color, back_color, link_color, visited_color)


if __name__ == "__main__":
    main()