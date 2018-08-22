from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # 使用它来操作数据库


app = Flask(__name__)


class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    app.config["SQLALCHEMY_ECHO"] = True


app.config.from_object(Config)
db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),unique=True)
    us = db.relationship("User", backref="role")


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))


@app.route("/")
def index():
    pass


if __name__ == '__main__':
    # 删除所有数据
    db.drop_all()

    # 创建表
    db.create_all()

    user1 = User()  # 实例化对象，也就是创建一个数据
    user1.name = "ly"
    user1.email = "456@qq.com"
    user1.password = 123456
    #
    # # 把数据储存到数据库
    db.session.add(user1)   # 添加指令
    db.session.commit()   # 提交指令

    app.run()


