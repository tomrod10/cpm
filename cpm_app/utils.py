import random
import colorsys
from PIL import Image
from typing import Union, List, Tuple


def get_color_from_img(file: str) -> Tuple[float, float, float]:
    with Image.open(file) as im:
        im = im.convert("RGB")
        width, height = im.size
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        pixel_data = im.getpixel((x,y))

    if isinstance(pixel_data, tuple) and len(pixel_data) == 3:
        r, g, b = pixel_data[0]/255.0, pixel_data[1]/255.0, pixel_data[2]/255.0
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        return (h, l, s)
    else:
        raise ValueError("Unsupported image mode or grayscale image detected. Only color images supported.")

# ColorPalette = List[Tuple[Union[float, int], Union[float, int], Union[float, int]]]
ColorPalette = List[int]

# TODO: Write a docstring explaining this function and how we are calculcating steps
# Union[ColorPalette, dict[str, ColorPalette]
def make_monochromatic_color_palette(hls: Tuple[float, float, float], format: str) -> ColorPalette: #WIP
    # Hue: Change 2 between 1 - 3 points
    # Light: Increment each 8 to 13 points | Dark to Light == Low to High
    # Sat: Vary +- 5 to 15 point of any 2
    # holds 5 lists containing HLS values

    steps = 5
    hls_cp = list()
    h, l, s = hls

    if format == "h":
        new_h = h
        new_l = 0.0
        new_s = s

        SINGLE_UNIT = 0.00990099 # Equivalent to single unit (1) in the 0 - 100 range
        SINGLE_HUE_UNIT = 0.0027777777 # Equivalent to single unit in the 0 - 360 range
        RANGE_CEIL = 0.9999999999999999  # Equivalent to the max unit in the 0 - 100 range
        for i in range(steps):
            if i == 0 or i == 4:
                # Fix: Double check if hue range in HLS format is from 0 - 360
                variation = random.uniform(SINGLE_HUE_UNIT, (SINGLE_HUE_UNIT * 3.0)) # between 1 - 3 in in range of 0 - 100
                if h + variation > RANGE_CEIL:
                    new_h = h - variation
                else:
                    new_h = h + variation

            if i == 1 or i == 3:
                variation = random.uniform((SINGLE_UNIT * 5.0), (SINGLE_UNIT * 25.0)) # between 5 - 25 in in range of 0 - 100
                if s + variation > RANGE_CEIL:
                    new_s = s - variation
                else:
                    new_s = s + variation

            new_l += random.uniform((SINGLE_UNIT * 8.0), (SINGLE_UNIT * 20.0)) # between 8 - 20 in in range of 0 - 100

            # print(f"LOOP -> h: {h}, l: {l}, s: {s} | new_h: {new_h}, new_l: {new_l}, new_s: {new_s}")
            # convert back to RGB
            print(f"LOOP -> new_h: {new_h}, new_l: {new_l}, new_s: {new_s}")
            r, g, b = colorsys.hls_to_rgb(new_h, new_l, new_s)

            hls_cp.append([int(r * 255), int(g * 255), int(b * 255)])

        return hls_cp

    # elif format == "r":
    #     return [(2,2,2),
    #             (2,2,2),
    #             (2,2,2),
    #             (2,2,2),
    #             (2,2,2)]
    # elif format == "":
    #     formats = {
    #         "hls_values": [(0.2,0.2,0.2),
    #                     (0.2,0.2,0.2),
    #                     (0.2,0.2,0.2),
    #                     (0.2,0.2,0.2),
    #                     (0.2,0.2,0.2)],
    #         "rgb_values": [(2,2,2),
    #                     (2,2,2),
    #                     (2,2,2),
    #                     (2,2,2),
    #                     (2,2,2)]
    #     }
    #     return formats
    else:
        raise Exception("Unsupported color format")

# Union[HLS, RGB, dict[HLS, RGB]]




def main():
    fp = input("Enter file path: ")
    get_color_from_img(fp)

if __name__ == "__main__":
    main()
