from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "index page"


# 钩子 @之后的都为固定写法  函数是人为定义的


# 在index函数执行完成之后会执行（如果前面的程序报错，就不会执行）
@app.after_request
def handler_after_request(response):
    print("handler_after_request")
    return response


# 在index函数执行完成之后执行，afte_request执行完成最后执行
# 括号的参数为服务器出现错误的信息
@app.teardown_request
def handler_teardown_request(e):
    print("handler_teardown_request")

# 第一次请求执行（并且只会执行一次，再次请求不会执行）
@app.before_first_request
def handlder_before_first_request():
    print("handler_before_first_request")


@app.before_request
def handler_before_request():
    print("handler_before_request")


if __name__ == '__main__':
    app.run()
