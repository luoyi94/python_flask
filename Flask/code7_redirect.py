from flask import Flask,redirect,url_for

app = Flask(__name__)
@app.route("/jd")
def demo1():
    return "京东"

@app.route("/360buy")
def demo2():
    return redirect(url_for("demo1"))


if __name__ == '__main__':
    app.run()



