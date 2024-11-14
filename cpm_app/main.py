import os
import sys
import magic
import mimetypes
import platform

from PIL import Image, UnidentifiedImageError

def main():
    color_schemes = ["mono", "alog", "comp", "scomp"]
    try:
        while True:
            file_name = input("Enter name of the file you wish to generate a palette from: ")
            if not len(file_name) or not os.path.isfile(file_name):
                print("Filename not found or invalid! Try again")
                continue

            color_scheme = input("Enter color scheme you wish to use: ")
            if color_scheme not in color_schemes:
                print("Invalid color scheme! Try again")
                continue
                # raise ValueError("Invalid color scheme")

            color_format = input("For color palette format enter r for RGB, h for HSL, omit for both: ")
            # image = Image.open(file_name)
            if color_format == "r":
                # rgb = generate_rgb_color_palette(image)
                # # more code to generate colored squares using generated cp
                print("[rgb values..., ...]")
            if color_format == "h":
                # hsl = generate_hsl_color_palette(image)
                # more code to generate colored squares using generated cp
                print("[hsl values..., ...]")
            if not color_format:
                # rgb = generate_rgb_color_palette(image)
                # hsl = generate_hsl_color_palette(image)
                # # more code to generate colored squares using generated cp
                print("[rgb, values..., ...]")
                print("[hsl, values..., ...]")
            else:
                print("Invalid color format! Try again")
                continue

            generate_another_cp = input("Would you like to generate another color palette? (y/n): ")
            if generate_another_cp == "y":
                continue
            else:
                sys.exit("Stay creative, bye!")

    except ValueError as e:
        print(e, file=sys.stdout)
    except KeyboardInterrupt:
        sys.exit("\nStay creative, bye!")

if __name__ == "__main__":
    main()
