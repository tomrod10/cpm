import random
import colorsys
from PIL import Image, ImageDraw
from typing import List, Tuple, Dict


# HLS units and range
SINGLE_UNIT = 0.00990099  # Equivalent to single unit in the 0 - 100 range
SINGLE_HUE_UNIT = 0.0027777777  # Equivalent to single unit in the 0 - 360 range
RANGE_CEIL = (
    0.9999999999999999  # Equivalent to the max value in our number range
)

STEPS = 5


def get_color_from_img(file: str) -> Tuple[float, float, float]:
    with Image.open(file) as im:
        im = im.convert("RGB")
        width, height = im.size
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        pixel_data = im.getpixel((x, y))

    if isinstance(pixel_data, tuple) and len(pixel_data) == 3:
        r, g, b = (
            pixel_data[0] / 255.0,
            pixel_data[1] / 255.0,
            pixel_data[2] / 255.0,
        )
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        return (h, l, s)
    else:
        raise ValueError(
            "Unsupported image mode or grayscale image detected. Only color images supported."
        )


ColorPalette = Dict[str, List[List[int]]]


def make_mono_color_palette(
    hls: Tuple[float, float, float], format: str
) -> ColorPalette:
    """
    Returns a 5-step monochromatic color palette in HLS and RGB color formats

        Parameters:
            hls (Tuple[float, float, float]): A tuple of floats that represents an HLS color
            format (string): A string representing color format to return to user. 'h' for HLS, 'r' for RGB and None or 'b' for both HLS and RGB

        Returns:
            color_palette (Dict[str, List[List[int]]]): A dict with a list containing lists of integers as the value for its keys
    """
    color_palette = {"h": [], "r": []}
    h, l, s = hls

    if format in ("r", "h", "rh"):
        new_h = h
        new_l = 0.0
        new_s = s

        for i in range(STEPS):
            if i == 0 or i == 4:
                variation = random.uniform(
                    SINGLE_HUE_UNIT, (SINGLE_HUE_UNIT * 3.0)
                )
                if h + variation > RANGE_CEIL:
                    new_h = h - variation
                else:
                    new_h = h + variation

            if i == 1 or i == 3:
                variation = random.uniform(
                    (SINGLE_UNIT * 5.0), (SINGLE_UNIT * 25.0)
                )
                if s + variation > RANGE_CEIL:
                    new_s = s - variation
                else:
                    new_s = s + variation

            new_l += random.uniform((SINGLE_UNIT * 8.0), (SINGLE_UNIT * 20.0))

            color_palette["h"].append(
                [int(new_h * 360), int(new_l * 100), int(new_s * 100)]
            )
            # convert back to RGB
            r, g, b = colorsys.hls_to_rgb(new_h, new_l, new_s)
            color_palette["r"].append(
                [int(r * 255), int(g * 255), int(b * 255)]
            )
        return color_palette
    else:
        raise ValueError("Unsupported color format")


def make_alog_color_palette(
    hls: Tuple[float, float, float], format: str
) -> ColorPalette:
    """
    Returns a 5-step analogous color palette in HLS and RGB color formats

        Parameters:
            hls (Tuple[float, float, float]): A tuple of floats that represents an HLS color
            format (string): A string representing color format to return to user. 'h' for HLS, 'r' for RGB and None or 'b' for both HLS and RGB

        Returns:
            color_palette (Dict[str, List[List[int]]]): A dict with a list containing lists of integers as the value for its keys
    """
    color_palette = {"h": [], "r": []}
    h, l, s = hls

    if format in ("r", "h", "rh"):
        new_h = h
        new_l = 0.0
        new_s = s

        for i in range(STEPS):
            end_variation = random.uniform(
                (SINGLE_UNIT * 18), (SINGLE_UNIT * 27)
            )
            center_variation = random.uniform(
                (SINGLE_UNIT * 7), (SINGLE_UNIT * 15)
            )
            if i == 0:
                new_h = h - end_variation
            if i == 1:
                new_h = h - center_variation
            if i == 2:
                new_h = h
            if i == 3:
                new_h = h + center_variation
            if i == 4:
                new_h = h + end_variation

            # TODO: This might need some tweaking
            if new_h > RANGE_CEIL:
                new_h -= RANGE_CEIL
            if new_h < 0:
                new_h += RANGE_CEIL

            if i == 1 or i == 3:
                variation = random.uniform(
                    (SINGLE_UNIT * 5.0), (SINGLE_UNIT * 25.0)
                )
                if s + variation > RANGE_CEIL:
                    new_s = s - variation
                else:
                    new_s = s + variation

            new_l += random.uniform((SINGLE_UNIT * 8.0), (SINGLE_UNIT * 20.0))

            color_palette["h"].append(
                [int(new_h * 360), int(new_l * 100), int(new_s * 100)]
            )
            # convert back to RGB
            r, g, b = colorsys.hls_to_rgb(new_h, new_l, new_s)
            color_palette["r"].append(
                [int(r * 255), int(g * 255), int(b * 255)]
            )
        return color_palette
    else:
        raise ValueError("Unsupported color format")


def draw_color_palette(color_palette: List[List[int]]) -> None:
    bg_im = Image.new("RGB", (1000, 200), (83, 83, 83))
    bg_draw = ImageDraw.Draw(bg_im)

    x0, y0, x1, y1 = 0, 0, 200, 200
    for c1, c2, c3 in color_palette:
        bg_draw.rectangle((x0, y0, x1, y1), (c1, c2, c3))
        x0 += 200
        x1 += 200
    bg_im.show()
    return None


# TODO: Pretty print this in a nice format
def process_and_print_res(
    fn: str, cs: str, cf: str, mc: Tuple[float, float, float], cp: ColorPalette
) -> None:
    print("\n")
    print(f"File: {fn}")
    print(f"Color Scheme: {cs}")
    print(f"Color Format: {cf}")

    hls = [int(mc[0] * 360), int(mc[1] * 100), int(mc[2] * 100)]
    r_float, g_float, b_float = colorsys.hls_to_rgb(mc[0], mc[1], mc[2])
    rgb = [int(r_float * 255), int(g_float * 255), int(b_float * 255)]

    if cf == "h":
        print(f"Main HLS Color: {hls}")
    if cf == "r":
        print(f"Main RGB Color: {rgb}")
    if cf == "rh":
        print(f"Main Colors: RGB {rgb} | HLS {hls}")
        print(f"Color palettes:\nHLS: {cp['h']}\nRGB: {cp['r']}")
    else:
        print(f"Color palette: {cp[cf]}")
    draw_color_palette(cp["r"])
