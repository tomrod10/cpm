import sys
from cli_flow.utils import get_color_format, get_user_file, get_color_scheme
from cpm_app.utils import get_color_from_img


def interactive_flow():
    valid_exts = [".jpg", ".jpeg", ".png"]
    color_schemes = ["mono", "alog", "comp", "scomp"]
    color_formats = ["r", "h", ""]
    try:
        file_name = get_user_file(valid_exts)
        color_scheme = get_color_scheme(color_schemes)
        color_format = get_color_format(color_formats)
        main_color = get_color_from_img(file_name)
        # TODO: Write function to generate color palette
            # generate_color_palette(cs: str, cf: str)

        # TODO: Pretty print this in a nice user friendly format
        print("\n")
        print(f"File: {file_name}")
        print(f"Color Scheme: {color_scheme}")
        print(f"Color Format: {color_format}")
        print("Color palette: <rgb and/or hsl values> <colored squares>")


    except ValueError as e:
        print(e, file=sys.stdout)
    except KeyboardInterrupt:
        sys.exit("\nStay creative, bye!")
    return None

if __name__ == "__main__":
    interactive_flow()
