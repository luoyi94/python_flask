from flask import Flask,make_response
from flask import request

app = Flask(__name__)


@app.route("/set_cookie")
def set_cookie():
    resp = make_response("设置cookie成功")
    resp.set_cookie("name","itheima",max_age=7200)
    resp.set_cookie("city","sz")
    return resp


@app.route("/get_cookie")
def get_cookie():
    name = request.cookies.get("name")
    return "获取到cookie的值 = " + name


if __name__ == '__main__':
    app.run()




