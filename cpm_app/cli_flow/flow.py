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

        hls = [int(main_color[0] * 360), int(main_color[1] * 100), int(main_color[2] * 100)]
        rf, gf, bf = colorsys.hls_to_rgb(main_color[0], main_color[1], main_color[2])
        rgb = [int(rf * 255), int(gf * 255), int(bf * 255)]
        if color_format == "h":
            print(f"Main HLS Color: {hls}")
        if color_format == "r":
            print(f"Main RGB Color: {rgb}")
        if color_format == 'rh':
            print(f"Main Colors: RGB {rgb} | HLS {hls}")
            print(f"Color palette:\nHLS: {mono_cps['h']}\nRGB: {mono_cps['r']}")
        else:
            print(f"Color palette: {mono_cps[color_format]}")
        draw_color_palette(mono_cps['r'])

    except ValueError as e:
        print(e, file=sys.stdout)
    except KeyboardInterrupt:
        sys.exit("\nStay creative, bye!")
    return None

if __name__ == "__main__":
    interactive_flow()
