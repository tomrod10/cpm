import random
import colorsys
from PIL import Image


def get_random_color_from_img(file: str) -> tuple[float, float, float]:
    im = Image.open(file)
    width, height = im.size
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    pixel_data = im.getpixel((x,y))

    if isinstance(pixel_data, tuple):
        r, g, b = pixel_data[0]/255.0, pixel_data[1]/255.0, pixel_data[2]/255.0
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        return (h, l, s)
    elif isinstance(pixel_data, int):
        grs_1 = grs_2 = grs_3 = pixel_data / 255.0
        return (grs_1, grs_2, grs_3)
    else:
        raise ValueError("Unsupported color format or image mode.")


def main():
    fp = input("Enter file path: ")
    get_random_color_from_img(fp)

if __name__ == "__main__":
    main()
