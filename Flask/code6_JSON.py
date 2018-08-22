import json

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    data = {
        "name": "python",
        "age": 18
    }
    return jsonify(data)
    # result = json.dumps(data)
    # return result, 200, {"Content-Type":"application/json"}


if __name__ == '__main__':
    app.run()
