from flask import Flask,redirect,url_for
from flask_script import Manager

app = Flask(__name__)

# 把flask对象交给manager进行管理
manager = Manager(app)


@app.route("/jd")
def demo1():
    return "index page"


@app.route("/360buy")
def demo2():
    return redirect(url_for("demo1"))


if __name__ == '__main__':
    manager.run()




