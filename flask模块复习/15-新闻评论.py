# 用户如果在登录的情况下，可以进行评论，未登录，#
# 点击评论弹出登录框
# 用户可以直接评论当前新闻，也可以回复别人发的评论用户A回复用户B的评论之后，
# 用户A的评论会当做一条主评论进行显示，
#下面使用灰色框将用户B的评论显示

@news_blue.route("/news_comment", methods = ["POST"])
@user_login_data
def news_comment():
    user = g.user
    if not user :
        return jsonify(errno=RET.SESSIONERR, errmsg="没有登陆")

    news_id = request.json.get("user_id")
    comment_str = request.json.get("comment")
    parent_id = request.json.get("parent_id")
    # 评论，需要知道获取评论的是哪一条新闻
    news = News.query.get(user_id)

    # 创建新记录  实例化模型类对象
    comment = Comment()
    comment.user_id =  user.id
    comment.news_id = news.id
    comment.content = comment_str
    # 判断当前评论是否父类，区分改楼和单个评论
    if parent_id:
        comment.parent_id = parent_id
    # 添加
    db.session.add(comment)
    # 生效
    db.session.commit()
    return jsonify(errno=RET.OK, errmsg="评论成功", data=commetn.to_dict())





