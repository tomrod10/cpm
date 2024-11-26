import random
import colorsys
from PIL import Image
# maybe import for converting HSL to RGB to Hex


def get_random_color_from_img(file: str) -> tuple[float, float, float]:
    im = Image.open(file)
    width, height = im.size
    print(f"Size: W: {width}, H: {height}")
    x = random.randint(0, width)
    y = random.randint(0, height)

    print(f"Rand Coords: x: {x}, y: {y}")
    color_r = im.getpixel((x,y))
    print(f"RGB: {color_r}")

    (r, g, b) = color_r[0]/255.0, color_r[1]/255.0, color_r[2]/255.0
    print(f"abc: {r}, {g}, {b}")
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    print(f"hsl: {h}, {l}, {s}")

    r_im = Image.new(mode="RGB", size=(width, height), color=color_r)
    # h_im = Image.new(mode="HSV", size=(w, h), color=(h, s, l))
    r_im.show()
    # h_im.show()

    return (h, l, s)


def main():
    fp = input("Enter file path: ")
    get_random_color_from_img(fp)

if __name__ == "__main__":
    main()
