#!/bin/usr/env python
"""
Make bricks lab from code bat
"""


def make_bricks(small, big, goal):
    if (goal > big * 5 + small):
        return False

    if (goal % 5 > small):
        return False

    return True







