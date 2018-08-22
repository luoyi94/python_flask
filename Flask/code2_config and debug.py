from flask import Flask

app = Flask(__name__)


class Config(object):
    DEBUG = True

app.config.from_object(Config)
# app.config.from_pyfile("config.cfg")


@app.route("/")
def index():
    a = 1 / 0
    return "index page"

if __name__ == '__main__':
    app.run()