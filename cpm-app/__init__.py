from flask import Flask, render_template


def create_app():
    app = Flask("CPM", instance_relative_config=True)

    if __name__ == "__main__":
        app.run()

    from . import views
    views.register_routes(app)

    return app
