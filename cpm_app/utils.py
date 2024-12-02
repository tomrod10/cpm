import random
import colorsys
from typing import Union
from dataclasses import dataclass
from PIL import Image


def get_color_from_img(file: str) -> tuple[float, float, float]:
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

@dataclass
class HLS:
    hls_values: tuple[tuple[float, float, float],
                        tuple[float, float, float],
                        tuple[float, float, float],
                        tuple[float, float, float],
                        tuple[float, float, float]]

@dataclass
class RGB:
    rgb_values: tuple[tuple[int, int, int],
                        tuple[int, int, int],
                        tuple[int, int, int],
                        tuple[int, int, int],
                        tuple[int, int, int]]

def make_monochromatic_color_palette(hls: tuple, **kwargs) -> Union[HLS, RGB, dict[HLS, RGB]]: #WIP
    if True:

        return HLS(((0.2,0.2,0.2),
                    (0.2,0.2,0.2),
                    (0.2,0.2,0.2),
                    (0.2,0.2,0.2),
                    (0.2,0.2,0.2)))

# Union[HLS, RGB, dict[HLS, RGB]]




def main():
    fp = input("Enter file path: ")
    get_color_from_img(fp)

if __name__ == "__main__":
    main()
