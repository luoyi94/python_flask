from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("code15_filter.html")

# 定义实现功能的函数
def do_setp2(my_filter):
    return my_filter[::2]
# (函数名，自定义过滤器的名字)
app.add_template_filter(do_setp2,"li")

if __name__ == '__main__':
    app.run()
