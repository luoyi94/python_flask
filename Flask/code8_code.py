from flask import Flask
app = Flask(__name__)


@app.route("/demo/<int:id>")
def index(id):
    return "index page = %s" % id


if __name__== "__main__":
    app.run()