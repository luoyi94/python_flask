from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def login():
    # 提取表单数据
    name = request.form.get("name")
    age = request.form.get("age")
    # 提取？后面的参数
    city = request.args.get("city")

    return "name = %s, age = %s, city = %s" % (name,age,city)


if __name__ == '__main__':
    app.run()


