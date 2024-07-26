import os

from flask import Flask, render_template


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # maximum file size 25 MB
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY"), MAX_CONTENT_LENGTH=25 * 1024 * 1024
    )

    from . import upload
    app.register_blueprint(upload.bp)
    app.add_url_rule(rule="/", endpoint="index")

    return app
