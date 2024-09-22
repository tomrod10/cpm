import io
import sys

from flask import Blueprint, flash, redirect, render_template, request, url_for
from PIL import Image, UnidentifiedImageError

from cpm_app.utils import img_to_base64, remove_metadata

bp = Blueprint("upload", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/upload", methods=["GET", "POST"])
def upload_image_file():
    if request.method == "POST":
        # check if file is in request.files
        if "file" not in request.files:
            flash("Missing file")
            return redirect(url_for("index"))

        file = request.files["file"]
        # check for filename
        if not file.filename:
            flash("No file selected")
            return "<h1>No file selected or found</h1>"

        try:
            # check it's a valid image with Pillow
            buffer = Image.open(io.BytesIO(file.stream.read()))
            buffer.seek(0)
            buffer.verify()
            # img.show()
            img_without_meta = remove_metadata(buffer)
            img_str = img_to_base64(img_without_meta, img.format)
            # print(img_str, file=sys.stderr)
            return render_template(
                "upload.html", image_data=img_str, image=file, fmt=img.format
            )
        except FileNotFoundError:
            flash("Image file not found")
        except UnidentifiedImageError as e:
            flash(f"{e}")

        # TODO: check to see if I can call generate_color_palette
        # after all these steps instead of having the user click "generate"


@bp.route("/generate", methods=["GET", "POST"])
def generate_color_palette():
    pass
