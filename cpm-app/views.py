from flask import Flask, flash, render_template, request, url_for


def register_routes(app):
    @app.route("/", methods=["GET", "POST"])
    def index():
        return render_template("index.html")

    @app.route("/upload", methods=["GET", "POST"])
    def upload_image_file():
        error = None
        if request.method == "GET":
            render_template("upload.html")

    @app.route("/generate", methods=["GET", "POST"])
    def generate_color_palette():
        pass
