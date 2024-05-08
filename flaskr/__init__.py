from flask import Flask


def create_app():
    app = Flask("CPM", instance_relative_config=True)
  
    @app.route("/hello")
    def hello():
        return "Hello World"

    return app


