from flask import Flask,render_template
from flask import request
from flask_wtf import FlaskForm
from wtforms import  StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,EqualTo

app = Flask(__name__)

# 加密
app.config["SECRET_KEY"] = "1ASDFASF"


# 定义表单类
class RegisterForm(FlaskForm):
    user_name = StringField(label="用户名",validators=[DataRequired("必须填写用户名")])
    password = PasswordField(label="密码",validators=[DataRequired("必须输入密码")])
    password2 = PasswordField(label="确认密码",validators=[DataRequired("必须再次输入密码"),EqualTo("password","两次密码必须一致")])
    submit = SubmitField(label="提交")


@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        data = RegisterForm()
        return render_template("code17_wtf.html",form_obj = data)
    else:
        data = RegisterForm()
        if data.validate_on_submit():
            print("注册成功")
            return "注册成功"
        else:
            return render_template("code17_wtf.html",form_obj = data)


if __name__ == '__main__':
    app.run()





