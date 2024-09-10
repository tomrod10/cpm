import base64
import sys
from io import BytesIO

from PIL import Image


def remove_metadata(img):
    img_data = img.getdata()
    new_img = Image.new(img.mode, img.size)
    new_img.putdata(img_data)
    return new_img


def img_to_base64(img, format):
    buffered = BytesIO()
    img.save(buffered, format)
    img_value = buffered.getvalue()
    img_encoded_base64 = base64.b64encode(img_value)
    img_decoded = img_encoded_base64.decode("utf-8")
    # print(img_decoded, file=sys.stdout)
    # img_str = f"data:image/{format};base64, {base64.b64encode(buffered.getvalue())}"
    img_str = f"data:image/{format};base64, {img_decoded}"
    return img_str
