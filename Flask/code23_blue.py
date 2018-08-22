from flask import Flask
from user.views import user_blue

app = Flask(__name__)

app.register_blueprint(user_blue)


@app.route("/passport")
def passport():
    return "passport"


@app.route("/news")
def news():
    return "news"


@app.route("/")
def index():
    return "index page"


if __name__ == '__main__':
    print(app.url_map)
    app.run()


