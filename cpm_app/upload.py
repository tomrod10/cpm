import sys
import hashlib
import datetime
import magic
import mimetypes

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
        safe_filename = ""
        if file:
            safe_filename = (
                secure_filename(file.filename)
                + hashlib.shake_128(safe_filename.encode()).hexdigest(5)
                + str(datetime.datetime.today())
            )
            print(safe_filename)

        # check MIME type is in (JPG, JPEG, PNG)
        mime = magic.from_buffer(file.read(), mime=True)
        ext = mimetypes.guess_extension(mime)
        if ext not in (".jpg", ".png", ".jpeg"):  # is PIL.Image.format better?
            raise ValueError("Invalid file type uploaded")

        # create new image
        # use safe_filename
        # remove EXIF / metadata - Image.Exif class
        # convert to 24bit lossless PNG
        # save under temp/ dir
        # open and display image for debugging

        # check for filename
        if not safe_filename:
            flash("No file selected")
            return "<h1>No file selected or found</h1>"
        print(secure_filename(file.filename), file=sys.stdout)

        try:
            return render_template(
                "upload.html", image_data=image, name=file.filename, fmt=image.format
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
