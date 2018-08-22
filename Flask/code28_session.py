from flask import Flask,session


app = Flask(__name__)

app.config["SECRET_KEY"] = "fasdfasfkjaf"


@app.route("/set_session")
def set_session():
    session["name"] = "itcast"
    return "设置session成功"


@app.route("/get_session")
def get_session():
    name = session.get("name")
    return name


if __name__ == '__main__':
    app.run(debug=True)







