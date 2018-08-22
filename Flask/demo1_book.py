from flask import Flask,render_template
from flask import redirect
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)


class Config(object):
    # 加密
    SECRET_KEY = "ASDFASDF"
    # 连接数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/auth_book_1"
    SQLALCHEMY_TRACK_MODIFICATIONS = False   # 关闭型号追踪
    # app.config["SQLALCHEMY_ECHO"] = True   # 打印原始数据  显示mySQL语句

# 写入配置
app.config.from_object(Config)
# 初始化数据库的对象
db = SQLAlchemy(app)

# 定义作者的模型 并且继承  一的一方
class Author(db.Model):
    # 表名
    __tablename__ = "authors"
    # 定义字段
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128))
    # 链接多的那边
    books = db.relationship("Book", backref="author")


# 定义书的模型   多的一方
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128))
    # 外键
    author_id = db.Column(db.Integer,db.ForeignKey("authors.id"))


# 传过来的为作者id
@app.route("/delete_author/<author_id>")
def delete_author(author_id):
    # 根据前端传过来的作者id查到作者
    author = Author.query.get(author_id)
    # 找到作者对应的所有书 并删除
    Book.query.filter(Book.author_id == author.id).delete()
    # 再删除作者
    db.session.delete(author)
    db.session.commit()

    # 删除后重定向主页面
    return redirect(url_for("index"))


# 根据传入的书名id
@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    book = Book.query.get(book_id)

    db.session.delete(book)
    db.session.commit()

    # author_id =
    # if Author.query.get()

    return redirect(url_for("index"))


# wtf表单
class AuthorBookForm(FlaskForm):
    author_name = StringField(label="作者",validators=[DataRequired("请输入作者的名字")])
    book_name = StringField(label="书名",validators=[DataRequired("请输入书的名字")])
    submit = SubmitField("添加")


@app.route("/",methods=["GET","POST"])
def index():
    # 实例化表单对象
    form = AuthorBookForm()

    # 点击添加按钮，添加数据到数据库
    if form.validate_on_submit():
        # 获取作者,书名输入表单中的数据
        author_name = form.author_name.data
        book_name = form.book_name.data

        print(author_name)
        print(book_name)
        # 实例化一个作者对象
        author = Author()
        # 赋值给对象数据
        author.name = author_name
        # 提交数据到数据库
        db.session.add(author)
        db.session.commit()

        # 实例化一个书名对象，并赋值提交到数据库鲁
        book = Book()
        book.name = book_name
        book.author_id = author.id
        db.session.add(book)
        db.session.commit()

    # 获取到所有的作者
    authors = Author.query.all()

    # 展示页面  并把表单对象传出
    return render_template("demo1_book.html",form=form,authors = authors)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    # 生成数据
    au1 = Author(name="老王")
    au2 = Author(name="老依")
    au3 = Author(name="老刘")
    au4 = Author(name="老罗")
    # 数据提交给用户会话
    db.session.add_all([au1,au2,au3,au4])
    # 提交会话
    db.session.commit()
    # 创建书名，指定所属作者
    bk1 = Book(name="老王回忆录",author_id = au1.id)
    bk2= Book(name="老依回忆录", author_id=au2.id)
    bk3 = Book(name="老刘回忆录", author_id=au3.id)
    bk4 = Book(name="老王回忆录续集", author_id=au1.id)
    bk5 = Book(name="老了", author_id=au4.id)
    db.session.add_all([bk1,bk2,bk3,bk4,bk5])
    db.session.commit()



    app.run(debug=True)



