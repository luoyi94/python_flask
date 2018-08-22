from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        print("当前是GET请求")
    else:
        print("当前是POST请求")
    return "index page"


if __name__ == '__main__':
    print(app.url_map)
    # Map([ < Rule'/'(OPTIONS, POST, HEAD, GET) -> index >,
    # < Rule'/static/<filename>'(OPTIONS, HEAD, GET) -> static >])
    app.run()
