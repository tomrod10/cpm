import random
import colorsys
from PIL import Image


def get_random_color_from_img(file: str) -> tuple[float, float, float]:
    im = Image.open(file)
    width, height = im.size
    x = random.randint(0, width)
    y = random.randint(0, height)
    rgb = im.getpixel((x,y))

    if isinstance(rgb, tuple):
        (r, g, b) = rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        return (h, l, s)
    elif rgb is not None:
        grs_1 = grs_2 = grs_3 = rgb / 255.0
        return (grs_1, grs_2, grs_3)
    else:
        raise ValueError("Something went wrong! The color values are not in the expected format.")


def main():
    fp = input("Enter file path: ")
    get_random_color_from_img(fp)

if __name__ == "__main__":
    main()
