import sys
from cpm_app.cli_flow.utils import get_color_format, get_user_file, get_color_scheme

from cpm_app.utils import get_color_from_img, make_mono_color_palette, process_and_print_res


def interactive_flow() -> None:
    valid_exts = [".jpg", ".jpeg", ".png"]
    color_schemes = ["mono", "alog", "comp", "scomp"]
    color_formats = ["r", "h", ""]
    try:
        file_name = get_user_file(valid_exts)
        color_scheme = get_color_scheme(color_schemes)
        color_format = get_color_format(color_formats)
        main_color = get_color_from_img(file_name)
        color_palette = {}

        match color_scheme:
            case "mono":
                color_palette = make_mono_color_palette(main_color, color_format)
            case _:
                print("Default case. This feature is still a WIP")
                raise ValueError("Invalid color scheme. Try again!")

        process_and_print_res(file_name, color_scheme, color_format, main_color, color_palette)

    except ValueError as e:
        print(e, file=sys.stdout)
    except KeyboardInterrupt:
        sys.exit("\nStay creative, bye!")
    return None

if __name__ == "__main__":
    interactive_flow()
