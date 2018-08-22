from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def index():
    data = {
        "name":"ly",
        "age":18,
        "list":[1,2,3,4,5],
        "dict":{
            "city":"sz"
        }
    }
    return render_template("code14_template.html", data=data)

if __name__ == '__main__':
    app.run()