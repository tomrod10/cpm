import os
import sys

from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    # maximum file size 25 MB
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY"), MAX_CONTENT_LENGTH=25 * 1024 * 1024
    )

    tmp_file_path = os.getcwd() + "/cpm_app/temp"
    tmp_files = os.listdir(tmp_file_path)
    print(tmp_files, file=sys.stdout)

    for file in tmp_files:
        os.remove(tmp_file_path + "/" + file)

    print(tmp_files, file=sys.stdout)

    from . import upload

    app.register_blueprint(upload.bp)
    app.add_url_rule(rule="/", endpoint="index")

    return app
