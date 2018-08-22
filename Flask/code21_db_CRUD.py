from flask import Flask
from flask_sqlalchemy import SQLAlchemy   # 连接书库
from flask_migrate import Migrate,MigrateCommand  # 迁移框架
from flask_script import Manager  # 脚本script
app = Flask(__name__)



class Config(object):
    # 链接数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# 导入配置
app.config.from_object(Config)
# 实例化数据库对象
db = SQLAlchemy(app)

# 脚本script 托管
manager = Manager(app)   # 初始化

Migrate(app,db)  # 初始化迁移框架 (flask对象,数据库)
manager.add_command("ly",MigrateCommand)


# 角色表模型
class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128))
    # title = db.Column(db.String(128))
    # title02 = db.Column(db.String(128))
    # 于User关联，并且定义
    us = db.relationship("User",backref = "role")

    # 表示友好提示  --查询显示内容
    def __repr__(self):
        return "Role = %s" % self.name

# 用户表
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer,db.ForeignKey("roles.id"))

    def __repr__(self):
        return "User = %s" % self.name


@app.route("/")
def index():
    pass


if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    #
    # # 实例化数据
    # ro1 = Role(name='admin')
    # db.session.add(ro1)
    # db.session.commit()
    # 再次插入一条数据
    # ro2 = Role(name='ly1')
    # db.session.add(ro2)
    # db.session.commit()
    #
    # # 插入多条user数据
    # us1 = User(name='wang', email='wang@163.com', password='123456', role_id=ro1.id)
    # us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=ro2.id)
    # us3 = User(name='chen', email='chen@126.com', password='987654', role_id=ro2.id)
    # us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=ro1.id)
    # us5 = User(name='tang', email='tang@itheima.com', password='158104', role_id=ro2.id)
    # us6 = User(name='wu', email='wu@gmail.com', password='5623514', role_id=ro2.id)
    # us7 = User(name='qian', email='qian@gmail.com', password='1543567', role_id=ro1.id)
    # us8 = User(name='liu', email='liu@itheima.com', password='867322', role_id=ro1.id)
    # us9 = User(name='li', email='li@163.com', password='4526342', role_id=ro2.id)
    # us10 = User(name='sun', email='sun@163.com', password='235523', role_id=ro2.id)
    #
    # db.session.add_all([us1, us2, us3, us4, us5, us6, us7, us8, us9, us10])
    # db.session.commit()

    # 脚本执行
    manager.run()

