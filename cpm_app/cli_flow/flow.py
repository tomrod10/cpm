import sys
import os
import colorsys
from cpm_app.cli_flow.utils import get_color_format, get_user_file, get_color_scheme
from PIL import Image, ImageDraw

from cpm_app.utils import get_color_from_img, make_monochromatic_color_palette


def interactive_flow():
    valid_exts = [".jpg", ".jpeg", ".png"]
    color_schemes = ["mono", "alog", "comp", "scomp"]
    color_formats = ["r", "h", ""]
    try:
        file_name = get_user_file(valid_exts)
        color_scheme = get_color_scheme(color_schemes)
        color_format = get_color_format(color_formats)
        main_color = get_color_from_img(file_name)
        mono_cp = make_monochromatic_color_palette(main_color, color_format)
        # TODO: Write function to generate color palette
            # generate_color_palette(cs: str, cf: str)

        # TODO: Pretty print this in a nice user friendly format
        print("\n")
        print(f"File: {file_name}")
        print(f"Color Scheme: {color_scheme}")
        print(f"Color Format: {color_format}")
        print(f"Main Color: {colorsys.hls_to_rgb(main_color[0], main_color[1], main_color[2])}")
        print(f"Color palette: {mono_cp}")

        bg_im = Image.new("RGB", (1000, 200), (83, 83, 83))
        bg_draw = ImageDraw.Draw(bg_im)
        # create image with 5 200 x 200 px squares filled with colors from mono_cp

        x0, y0, x1, y1 = 0, 0, 200, 200
        for color in mono_cp:
            bg_draw.rectangle((x0, y0, x1, y1), (color[0], color[1], color[2]))
            x0 += 200
            x1 += 200
        bg_im.show()
        mc_im = Image.new("RGB", (200, 200), int(main_color[0]))
        mc_im.show()

    except ValueError as e:
        print(e, file=sys.stdout)
    except KeyboardInterrupt:
        sys.exit("\nStay creative, bye!")
    return None

if __name__ == "__main__":
    interactive_flow()
