# coding=utf-8
# coding = '_*_ utf-8 _*_'
from flask import Flask, current_app

app = Flask(__name__)


class Config(object):
    LY = "python"


app.config.from_object(Config)


@app.route("/")
def index():
    print(current_app.config.get("LY"))
    return "index page"


if __name__ == '__main__':
    app.run()
