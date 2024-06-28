import os

from flask import Flask, render_template


def create_app():
    app = Flask("CPM", instance_relative_config=True)

    # maximum file size 25 MB
    app.config["MAX_CONTENT_LENGTH"] = 25 * 1024 * 1024

    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY"), MAX_CONTENT_LENGTH=25 * 1024 * 1024
    )

    if __name__ == "__main__":
        app.run()

    from . import views

    views.register_routes(app)

    return app
