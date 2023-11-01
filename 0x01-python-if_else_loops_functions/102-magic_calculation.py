#!/usr/bin/python3
def magic_calculation(a, b, c):
    """Performs some calculations based on bytecode instructions."""
    if a < b:
        return c
    if c > b:
        return a + b
    return a * b - c
