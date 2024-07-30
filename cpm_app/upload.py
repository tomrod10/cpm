import io
import sys

from flask import Blueprint, flash, redirect, render_template, request, url_for
from PIL import Image, UnidentifiedImageError
from werkzeug.utils import secure_filename

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
            return "No file selected"

        # create a secure filename
        if file:
            filename = secure_filename(file.filename)
            flash(f"{filename}")

            try:
                # check it's a valid image with Pillow
                img = Image.open(io.BytesIO(file.stream.read()))
                img.show()
                img.verify()
                img_without_meta = remove_metadata(img)
                img_str = img_to_base64(img_without_meta, img.format)
                print(img_str, file=sys.stdout)
                print(img_str, file=sys.stderr)
                return render_template("upload.html", image_data=img_str, image=file)
            except FileNotFoundError:
                flash("Image file not found")
            except UnidentifiedImageError as e:
                flash(f"{e}")
        else:
            return "<h1>No file or file.name<h1/>"
            # process image to base64 image

            # return base64 image to frontend when requested

        # TODO: check to see if I can call generate_color_palette
        # after all these steps instead of having the user click "generate"
@bp.route("/generate", methods=["GET", "POST"])
def generate_color_palette():
    pass
