# 后端提供点赞和取消点赞功能
# 当用户点击未点赞按钮，执行点赞逻辑，向后端发起点赞请求，取消点赞则反之
# 在新闻显示完成之后，底部评论会根据当前登录用户显示是否点赞图标

@news_blue.route("/comment_like", methods=["POST"])
@user_login_data
def comment_like():
    user = g.user
    if not user:
        return jsonify(errno=RET.SESSIONERR, errmsg="请登录")

    comment_id = request.json.get("comment_id")
    news_id = request.json.get("news_id")
    action = request.json.get("action")

    """评论点赞：1，谁点赞,2，当前对那条新闻点赞"""
    comment = Comment.query.get(comment_id)

    if action == "add":
        # 根据字段值判断是点赞 还是取消
        # 点赞
        # 根据两个条件返回查询集  first()返回查询集第一个  没有则返回None
        comment_like = CommentLike.query.filter(CommentLike.comment_id==comment_id, CommentLike.user_id == user.id).first()
        if not comment_like:
            # 查询出来没有点赞才能点赞，已经点赞的只能取消点赞
            comment_like = CommentLike()
            comment_like.comment_id = comment_id
            comment_like.user_id = user_id
            # 添加
            db.session.add(comment_like)
            # 点赞数量加1
            comment.like_count += 1
    else:
        # 取消点赞
        comment_like = CommentLike.query.filter(CommentLike.comment_id==comment_id,CommentLike.user_id==user_id).first()
        if comment_like:
            # 只有当用户对该新闻是点赞状态才能取消
            db.session.delete(comment_like)
            # 点赞数量减1
            comment.like_count -= 1
    # 提交
    db.session.commit()
    return jsonify(errno=RET.OK, errmsg="点赞成功")


