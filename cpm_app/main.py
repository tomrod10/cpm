import os
import sys
import magic
import mimetypes
import platform

from PIL import Image, UnidentifiedImageError

def main():
    device_os = platform.system()
    print(f"OS: [{device_os}]")
    print(f"Current directory: {os.getcwd()}")

    color_schemes = ["monochromatic", "analogous", "complementary", "split complementary"]

    while True:
        try:
            file_name = input("Enter name of the file you wish to generate a palette from: ")
            color_scheme = input("Enter color scheme you wish to use: ")
            color_format = input("For color palette format enter r for RGB, h for HSL, omit for both: ")
            generate_another_cp = input("Would you like to generate another color palette? (y/n): ")

            if color_scheme not in color_schemes:
                print("Invalid color scheme! Try again")
                continue
                # raise ValueError("Invalid color scheme")

            if not len(file_name):
                print("Filename not found or invalid! Try again")
                continue
                # raise ValueError("Invalid file path")

            # image = Image.open(file_name)
            if color_format == "r":
                # rgb = generate_rgb_color_palette(image)
                # # more code to generate and colored squares using generated cp
                print("[rgb values..., ...]")
            if color_format == "h":
                # hsl = generate_hsl_color_palette(image)
                # more code to generate and colored squares using generated cp
                print("[hsl values..., ...]")
            if not color_format:
                # rgb = generate_rgb_color_palette(image)
                # hsl = generate_hsl_color_palette(image)
                # # more code to generate and colored squares using generated cp
                print("[rgb, values..., ...]")
                print("[hsl, values..., ...]")

            if generate_another_cp == "y":
                continue
            else:
                sys.exit("Stay creative, bye!")



        except ValueError as e:
            print(e, file=sys.stdout)

        sys.exit()

if __name__ != "__main__":
    main()
