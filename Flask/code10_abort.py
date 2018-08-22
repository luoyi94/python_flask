from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route("/")
def index():
    print("显示正常")
    abort(400)
    print("前面异常咯")
    return "index page"


@app.errorhandler(400)
def error_404_hanlder(err):
    return "页面找不到了"


if __name__ == '__main__':
    app.run()
