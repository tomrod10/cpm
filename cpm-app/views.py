import secrets
from PIL import Image
from flask import flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename


def register_routes(app):
    @app.route("/", methods=["GET", "POST"])
    def index():
        return render_template("index.html")

    @app.route("/upload", methods=["GET", "POST"])
    def upload_image_file():
        error = None
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
                unique_filename = f"{secrets.token_hex(8)}_{filename}"

                # check it's a valid image with Pillow
                try:
                    img = Image.open(filename)
                    img.verify()
                except FileNotFoundError:
                    flash("Image file not found")
                except PIL.UnidentifiedImageError as e:
                    flash(f"{e}")

                # strip metadata from image file
                else:
                    img.close()

                # process image to base64 image

                # return base64 image to frontend when requested

            # TODO: check to see if I can call generate_color_palette
            # after all these steps instead of having the user click "generate"
            return render_template("upload.html")

    @app.route("/generate", methods=["GET", "POST"])
    def generate_color_palette():
        pass
