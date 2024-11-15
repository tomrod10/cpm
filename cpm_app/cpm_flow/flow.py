import os
import sys
import magic
import mimetypes

def interactive_flow():
    valid_exts = [".jpg", ".jpeg", ".png"]
    color_schemes = ["mono", "alog", "comp", "scomp"]
    file_name, color_scheme, color_format, retry = "", "", "", ""
    try:
        while True:
            file_name = input("Enter name of the file you wish to generate a palette from: ")
            if not len(file_name) or not os.path.isfile(file_name):
                print("Filename not found or invalid! Try again")
                continue
            ext = mimetypes.guess_extension(magic.from_file(file_name, mime=True))
            if ext not in valid_exts:
                print("Invalid file extension! Try another")
                continue
            break

        while True:
            color_scheme = input("Enter color scheme you wish to use: ")
            if color_scheme not in color_schemes:
                print("Invalid color scheme! Try again")
                continue
            break

        while True:
            color_format = input("For color palette format enter r for RGB, h for HSL, omit for both: ")
            # image = Image.open(file_name)
            if color_format not in ["r", "h", ""]:
                print("Invalid color format! Try again")
                continue
            break

            # generate color palette at this point - NOT BEFORE!
        if color_format == "r":
            # rgb = generate_rgb_color_palette(image)
            # # more code to generate colored squares using generated cp
            print("[rgb values..., ...]")
        elif color_format == "h":
            # hsl = generate_hsl_color_palette(image)
            # more code to generate colored squares using generated cp
            print("[hsl values..., ...]")
        elif not color_format:
            # rgb = generate_rgb_color_palette(image)
            # hsl = generate_hsl_color_palette(image)
            # # more code to generate colored squares using generated cp
            print("[rgb, values..., ...]")
            print("[hsl, values..., ...]")
        else:
            raise ValueError(f"Color format {color_format} is invalid!")
    except ValueError as e:
        print(e, file=sys.stdout)
    except KeyboardInterrupt:
        sys.exit("\nStay creative, bye!")
    return None

if __name__ == "__main__":
    interactive_flow()
