from flask import Flask, render_template


def create_app():
    app = Flask("CPM", instance_relative_config=True)

    @app.route("/")
    def home():
        return render_template("base.html")

    if __name__ == "__main__":
        app.run()

    return app
