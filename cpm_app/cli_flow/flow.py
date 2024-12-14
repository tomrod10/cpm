import sys
import colorsys
from cpm_app.cli_flow.utils import get_color_format, get_user_file, get_color_scheme

from cpm_app.utils import get_color_from_img, make_monochromatic_color_palette, draw_color_palette


def interactive_flow():
    valid_exts = [".jpg", ".jpeg", ".png"]
    color_schemes = ["mono", "alog", "comp", "scomp"]
    color_formats = ["r", "h", ""]
    try:
        file_name = get_user_file(valid_exts)
        color_scheme = get_color_scheme(color_schemes)
        color_format = get_color_format(color_formats)
        main_color = get_color_from_img(file_name)
        mono_cps = make_monochromatic_color_palette(main_color, color_format)

        # TODO: Pretty print this in a nice format
        print("\n")
        print(f"File: {file_name}")
        print(f"Color Scheme: {color_scheme}")
        print(f"Color Format: {color_format}")
        # TODO: Fix main color and print HLS or RGB depending on user format input...geez!
        print(f"Main Color: {colorsys.hls_to_rgb(main_color[0], main_color[1], main_color[2])}")
        if isinstance(mono_cps, dict):
            print(f"Color palette:\nHLS: {mono_cps['h']}\nRGB: {mono_cps['r']}")
            draw_color_palette(mono_cps['r'])
        else:
            print(f"Color palette: {mono_cps}")
            draw_color_palette(mono_cps) # type: ignore

    except ValueError as e:
        print(e, file=sys.stdout)
    except KeyboardInterrupt:
        sys.exit("\nStay creative, bye!")
    return None

if __name__ == "__main__":
    interactive_flow()
