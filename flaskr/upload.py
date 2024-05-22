from flask import Flask

app = Flask("CPM")

@app.route("/upload")
def uploaded():
    return "Uploaded"
