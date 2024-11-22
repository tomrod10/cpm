import os
import magic

from typing import Union

def get_user_file(valid_exts: list[str]) -> str:
    while True:
        file_name = input("Enter name of the file you wish to generate a palette from: ")
        if not len(file_name) or not os.path.isfile(file_name):
            print("[Filename not found or invalid! Try again]")
            continue
        ext = magic.from_file(file_name, mime=True)
        if ext not in valid_exts:
            print("[Invalid file extension! Try another]")
            continue
        return file_name

def get_color_scheme(color_schemes: list[str]) -> str:
    while True:
        color_scheme = input("Enter color scheme you wish to use: ")
        if color_scheme not in color_schemes:
            print("[Invalid color scheme! Try again]")
            continue
        return color_scheme

def get_color_format(color_formats: list[str]) -> str:
    while True:
        color_format = input("For color palette format enter r for RGB, h for HSL, omit for both: ")
        if color_format not in color_formats:
            print("[Invalid color format! Try again]")
            continue
        break

    if color_format == "r":
        print("rgb")
        return "r"
    elif color_format == "h":
        print("hsl")
        return "h"
    elif not color_format:
        print("rgb and hsl")
        return "rh"
    else:
        raise ValueError(f"[Color format {color_format} is invalid!]")

# TODO: Write function to generate color palette
def generate_color_palette(cs: str, cf: str) -> Union[list[tuple], list[str]]:
    ...
