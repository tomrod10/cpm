import base64
from PIL import Image
from io import BytesIO


def remove_metadata(img):
    img_data = img.getdata()
    new_img = Image.new(img.mode, img.size)
    new_img.putdata(img_data)
    return new_img

def img_to_base64(img, format):
    buffered = BytesIO()
    img.save(buffered, format)
    img_str = f"data:image/{format};base64, {base64.b64encode(buffered.getvalue())}"
    return img_str
