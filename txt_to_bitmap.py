"""This module converts a text file to a bitmap image."""
import numpy as np

# Define 5x7 dot matrices for each character
char_matrices = {
    " ": [
        "  ",
        "  ",
        "  ",
        "  ",
        "  ",
        "  ",
        "  ",
    ],
    "A": [
        "  X  ",
        " X X ",
        "X   X",
        "XXXXX",
        "X   X",
        "X   X",
        "X   X",
    ],
    "B": [
        "XXXX ",
        "X   X",
        "X   X",
        "XXXX ",
        "X   X",
        "X   X",
        "XXXX ",
    ],
    "C": [
        " XXX ",
        "X   X",
        "X    ",
        "X    ",
        "X    ",
        "X   X",
        " XXX ",
    ],
    "D": [
        "XXXX ",
        "X   X",
        "X   X",
        "X   X",
        "X   X",
        "X   X",
        "XXXX ",
    ],
    "E": [
        "XXXXX",
        "X    ",
        "X    ",
        "XXX  ",
        "X    ",
        "X    ",
        "XXXXX",
    ],
    "F": [
        "XXXXX",
        "X    ",
        "X    ",
        "XXXX ",
        "X    ",
        "X    ",
        "X    ",
    ],
    "G": [
        " XXX ",
        "X   X",
        "X    ",
        "X  XX",
        "X   X",
        "X   X",
        " XXX ",
    ],
    "H": [
        "X   X",
        "X   X",
        "X   X",
        "XXXXX",
        "X   X",
        "X   X",
        "X   X",
    ],
    "I": [
        " XXX ",
        "  X  ",
        "  X  ",
        "  X  ",
        "  X  ",
        "  X  ",
        " XXX ",
    ],
    "J": [
        "    X",
        "    X",
        "    X",
        "    X",
        "X   X",
        "X   X",
        " XXX ",
    ],
    "K": [
        "X   X",
        "X  X ",
        "X X  ",
        "XX   ",
        "X X  ",
        "X  X ",
        "X   X",
    ],
    "L": [
        "X    ",
        "X    ",
        "X    ",
        "X    ",
        "X    ",
        "X    ",
        "XXXXX",
    ],
    "M": [
        "X   X",
        "XX XX",
        "X X X",
        "X   X",
        "X   X",
        "X   X",
        "X   X",
    ],
    "N": [
        "X   X",
        "XX  X",
        "X X X",
        "X  XX",
        "X   X",
        "X   X",
        "X   X",
    ],
    "O": [
        " XXX ",
        "X   X",
        "X   X",
        "X   X",
        "X   X",
        "X   X",
        " XXX ",
    ],
    "P": [
        "XXXX ",
        "X   X",
        "X   X",
        "XXXX ",
        "X    ",
        "X    ",
        "X    ",
    ],
    "Q": [
        " XXX ",
        "X   X",
        "X   X",
        "X   X",
        "X X X",
        "X  X ",
        " XX X",
    ],
    "R": [
        "XXXX ",
        "X   X",
        "X   X",
        "XXXX ",
        "X X  ",
        "X  X ",
        "X   X",
    ],
    "S": [
        " XXX ",
        "X   X",
        "X    ",
        " XXX ",
        "    X",
        "X   X",
        " XXX ",
    ],
    "T": [
        "XXXXX",
        "  X  ",
        "  X  ",
        "  X  ",
        "  X  ",
        "  X  ",
        "  X  ",
    ],
    "U": [
        "X   X",
        "X   X",
        "X   X",
        "X   X",
        "X   X",
        "X   X",
        " XXX ",
    ],
    "V": [
        "X   X",
        "X   X",
        "X   X",
        " X X ",
        " X X ",
        "  X  ",
        "  X  ",
    ],
    "W": [
        "X   X",
        "X   X",
        "X   X",
        "X X X",
        "X X X",
        "X X X",
        " X X ",
    ],
    "X": [
        "X   X",
        "X   X",
        " X X ",
        "  X  ",
        " X X ",
        "X   X",
        "X   X",
    ],
    "Y": [
        "X   X",
        "X   X",
        " X X ",
        "  X  ",
        "  X  ",
        "  X  ",
        "  X  ",
    ],
    "Z": [
        "XXXXX",
        "    X",
        "   X ",
        "  X  ",
        " X   ",
        "X    ",
        "XXXXX",
    ],
    ".": [
        "  ",
        "  ",
        "  ",
        "  ",
        "  ",
        "XX",
        "XX",
    ],
    "*": [
        "  X  ",
        " X X ",
        "  X  ",
        "XXXXX",
        "  X  ",
        " X X ",
        "  X  ",
    ],
    "#": [
        " X X ",
        " X X ",
        "XXXXX",
        " X X ",
        "XXXXX",
        " X X ",
        " X X ",
    ],
    "a": [
        "     ",
        "     ",
        " XXX ",
        "    X",
        " XXXX",
        "X   X",
        " XXXX",
    ],
    "b": [
        "X    ",
        "X    ",
        "X    ",
        "XXXX ",
        "X   X",
        "X   X",
        "XXXX ",
    ],
    "c": [
        "    ",
        "    ",
        " XXX",
        "X   ",
        "X   ",
        "X   ",
        " XXX",
    ],
    "d": [
        "    X",
        "    X",
        "    X",
        " XXXX",
        "X   X",
        "X   X",
        " XXXX",
    ],
    "e": [
        "     ",
        "     ",
        " XXX ",
        "X   X",
        "XXXXX",
        "X    ",
        " XXXX",
    ],
    "f": [
        "  XX ",
        " X  X",
        " X   ",
        "XXXX ",
        " X   ",
        " X   ",
        " X   ",
    ],
    "g": [
        "     ",
        "     ",
        " XXXX",
        "X   X",
        " XXXX",
        "    X",
        " XXX ",
    ],
    "h": [
        "X    ",
        "X    ",
        "X    ",
        "XXXX ",
        "X   X",
        "X   X",
        "X   X",
    ],
    "i": [
        " X ",
        "   ",
        "XX ",
        " X ",
        " X ",
        " X ",
        "XXX",
    ],
    "j": [
        "   X",
        "    ",
        "  XX",
        "   X",
        "   X",
        "X  X",
        " XX ",
    ],
    "k": [
        "X    ",
        "X    ",
        "X  X ",
        "X X  ",
        "XX   ",
        "X X  ",
        "X  XX",
    ],
    "l": [
        "X  ",
        "X  ",
        "X  ",
        "X  ",
        "X  ",
        "X  ",
        " XX",
    ],
    # "m": [
    #     "     ",
    #     "     ",
    #     "X   X",
    #     "XX XX",
    #     "X X X",
    #     "X   X",
    #     "X   X",
    # ],
    # 7x7 m
    "m": [
        "       ",
        "       ",
        " XX XX ",
        "X  X  X",
        "X  X  X",
        "X  X  X",
        "X     X",
    ],
    "n": [
        "     ",
        "     ",
        "XXXX ",
        "X   X",
        "X   X",
        "X   X",
        "X   X",
    ],
    "o": [
        "     ",
        "     ",
        " XXX ",
        "X   X",
        "X   X",
        "X   X",
        " XXX ",
    ],
    "p": [
        "     ",
        "     ",
        "XXXX ",
        "X   X",
        "XXXX ",
        "X    ",
        "X    ",
    ],
    "q": [
        "     ",
        "     ",
        " XXXX",
        "X   X",
        " XXXX",
        "    X",
        "    X",
    ],
    "r": [
        "     ",
        "     ",
        "X XX ",
        "XX  X",
        "X    ",
        "X    ",
        "X    ",
    ],
    "s": [
        "     ",
        "     ",
        " XXXX",
        "X    ",
        " XXX ",
        "    X",
        "XXXX ",
    ],
    "t": [
        "  X  ",
        "  X  ",
        "XXXXX",
        "  X  ",
        "  X  ",
        "  X X",
        "   XX",
    ],
    "u": [
        "     ",
        "     ",
        "X   X",
        "X   X",
        "X   X",
        "X   X",
        " XXXX",
    ],
    "v": [
        "     ",
        "     ",
        "X   X",
        "X   X",
        "X   X",
        " X X ",
        "  X  ",
    ],
    # "w": [
    #     "     ",
    #     "     ",
    #     "X   X",
    #     "X   X",
    #     "X X X",
    #     "XX XX",
    #     "X X X",
    # ],
    # 7x7 w
    "w": [
        "       ",
        "       ",
        "X     X",
        "X     X",
        "X  X  X",
        "X X X X",
        " XX XX ",
    ],
    "x": [
        "     ",
        "     ",
        "X   X",
        " X X ",
        "  X  ",
        " X X ",
        "X   X",
    ],
    "y": [
        "     ",
        "     ",
        "X   X",
        "X   X",
        " XXXX",
        "    X",
        " XXX ",
    ],
    "z": [
        "     ",
        "     ",
        "XXXXX",
        "   X ",
        "  X  ",
        " X   ",
        "XXXXX",
    ],
}


def char_to_np(char: str):
    """Converts a character to a numpy array"""
    # one "pixel" of space is added to the right of each character
    return np.array([list(line) + [" "] for line in char_matrices[char]])


def text_to_array(text):
    """Converts a text to a numpy array"""
    # check if all characters are valid
    for char in text:
        if char not in char_matrices:
            raise ValueError(f"Invalid character: '{char}' in '{text}'")

    banner = np.hstack([char_to_np(letter) for letter in text])
    if banner.shape[1] > 52:
        raise ValueError(f"Banner text is too long: '{banner.shape[1]}' > 52")
    return banner