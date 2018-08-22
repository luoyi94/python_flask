from flask import Flask

from werkzeug.routing import BaseConverter

app = Flask(__name__)


class RegexConverter(BaseConverter):
    regex = "[0-9]{3}"

app.url_map.converters["xxx"] = RegexConverter

@app.route("/user/<xxx:user_id>")
def index(user_id):
    return "返回的参数 = %s" % user_id


if __name__ == '__main__':
    app.run()

