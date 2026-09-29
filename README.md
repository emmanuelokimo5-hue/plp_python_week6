# PLP Python Week 6 - Safe Functions

## Files

- `safe_tools.py` - Contains three safe functions for division, number conversion, and dictionary lookup.
- `unbreakable.py` - Demonstrates how try/except can prevent invalid user input from crashing a program.
- `README.md` - Explains the assignment and the purpose of each file.

## Why can the if check not catch `abc` on its own?

An `if` check can test conditions, but converting `"abc"` to an integer with `int()` causes a `ValueError` before a normal numeric comparison can be completed. The `try/except` block catches this error and allows the program to continue running safely.
