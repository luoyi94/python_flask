
@news_blue.route('/<int:news_id>')
@user_login_data
def news_detail(news_id):

    # g对象可以理解一个盒子，或者一个容器
    # g变量应用了上下文的变量
    user = g.user
    if not user:
        return jsonify(errno=RET.SESSIONERR, errmsg="没有登录")

    """右边的热门新闻排序"""
    # 获取到热门新闻，通过点击事件进行倒叙排序，然后获取到前面10条新闻
    news_model_list = News.query.order_by(News.clicks.desc()).limit(10)
    news_dict = []

    for news in news_model_list:
        news_dict.append(news.to_dict())

    # 展示详情页面的新闻
    news_model = News.query.get(news_id)
    # 点击完成之后，新闻点击字段加1
    news_model.clicks += 1

    # 收藏新闻
    # 1，判断用户是否登陆
    is_collected = False
    if user:
        if news_model in user.collection_news:
            # 判断该用户是否已经收藏该新闻
            is_collected = True


    """查询当前新闻的所有评论"""
    # 根据新闻Id查询当前新闻的所有评论，按照时间倒叙分组
    comment_list = Comment.query.filter(Comment.news_id==news_id).order_by(Comment.create_time.desc()).all()
    comments = []
    for comment in comment_list:
        comment = comment.to_dict()
        comments.append(comment)

    """获取到所有点赞的数据"""
    comment_likes = []
    comment_like_ids = []
    if user:
        # 查询用户点赞了哪些评论
        comment_likes = CommentLike.query.filter(CommentLike.user_id==user.id).all()
        # 取出来所有点赞的id
        comment_like_ids = [ comment_like.comment_id for comment_like in comment_likes ]

    comment_dict_list = []
    for item in comment_list:
        comment_dict = item.todict()
        comment_dict["is_like"] = False
        # 判断用户是否点赞该评论
        if item.id in comment_like_ids:
            comment_dict["is_like"] = True
            comment_dict_list.append(comment_dict)


    data = {
        "user_info": user.to_dict() if user else None,
        "click_news_list": news_dict,
        "is_collected": is_collected,
        "news": news_model.to_dict(),
        "comment": comment_dict_list
    }

    return render_template('news/detail.html', data=data)




