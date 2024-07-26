import io

from flask import Blueprint, flash, redirect, render_template, request, url_for
from PIL import Image, UnidentifiedImageError
from werkzeug.utils import secure_filename

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
            return redirect(url_for("index")) # might have to add url_rule i think?

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
                img = Image.open(file.stream)
                img.verify()
                # TODO: extract this to util func ---
                img_data = img.getdata()
                img_without_exif = Image.new(img.mode, img.size)
                img_without_exif.putdata(img_data)
                # ---
                # save img data in memory buffer
                byte_arr = io.BytesIO()
                img_without_exif.save(byte_arr, format=img_without_exif.format)
                byte_arr.seek(0)
            except FileNotFoundError:
                flash("Image file not found")
            except UnidentifiedImageError as e:
                flash(f"{e}")
            else:
                img.close()

        else:
            return "<h1>No file or file.name<h1/>"
            # process image to base64 image

            # return base64 image to frontend when requested

        # TODO: check to see if I can call generate_color_palette
        # after all these steps instead of having the user click "generate"
        file_name = file.filename
        image_data = Image.open(file_name).load()
        return render_template("upload.html", image_data=image_data, image=file)

@bp.route("/generate", methods=["GET", "POST"])
def generate_color_palette():
    pass
