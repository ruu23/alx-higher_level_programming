#!/usr/bin/python3
def magic_string():
    magic_string.x = getatt(magic_string, 'n', 0) + 1
    return ", ".join(["BestSchool" for i in range (magic_string.x)])
