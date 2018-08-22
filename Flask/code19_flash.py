from flask import Flask,render_template,flash,g

app= Flask(__name__)


class Config(object):
    SECRET_KEY = "fasdfasljflaks"


app.config.from_object(Config)


@app.route("/")
def index():
    flash("请")
    flash("输")
    flash("入")
    flash("用户名")
    g.name = "ly"
    return render_template("code19_flash.html")


if __name__ == '__main__':
    app.run()



