from flask import Flask,request
app = Flask(__name__)


@app.route("/", methods=["post"])
def index():
    pic = request.files.get("pic")
    pic.save("./a.jpg")
    return "index page"


if __name__ == '__main__':
    app.run()



