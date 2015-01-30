#!/usr/bin/env python
"""
Improving raw_input

The raw_input() function can generate two exceptions: EOFError or KeyboardInterrupt on end-of-file(EOF) or canceled input.
Create a wrapper function, perhaps safe_input() that returns None rather rather than raising these exceptions, when the user enters ^C for Keyboard Interrupt, or ^D (^Z on Windows) for End Of File.
Update your mailroom program to use exceptions (and IBAFP) to handle malformed numeric input
"""
