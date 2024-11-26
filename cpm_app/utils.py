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
    # h, l, s = colorsys.rgb_to_hls(r, g, b)
    # print(f"hsl: {h}, {l}, {s}")

    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    h_int, s_int, v_int = int(h * 255), int(s * 255), int(v * 255)

    r_im = Image.new(mode="RGB", size=(width, height), color=color_r)
    h_im = Image.new(mode="HSV", size=(width, height), color=(h_int, s_int, v_int))
    r_im.show()
    h_im.show()

    # return (h, l, s)
    return


def main():
    fp = input("Enter file path: ")
    get_random_color_from_img(fp)

if __name__ == "__main__":
    main()
