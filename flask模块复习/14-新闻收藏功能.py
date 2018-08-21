# 进入到新闻详情页之后，如果用户已收藏该新闻，
# 则显示已收藏，点击则为取消收藏，# 反之点击收藏该新闻
# 因为只更新界面上部分元素，所以收藏和取消收藏的逻辑#

@news_blue.route("/news_collect", methods=["POST"])
@user_login_data
def news_collect():
    """新闻收藏"""
    user = g.user
    # 新闻id
    news_id = requst.json.get("news_id")
    # 点击事件
    action = requst.json.get("action")

    news = News.query.get(news_id)

    if action == "collect":
        # 根据该字段的值判断你是收藏还是取消收藏
        user.collection_news.append(news)
    else:
        # 取消收藏
        user.collection_news.remove(news)
    # 提交生效
    db.session.commit()
    return jsonify(errno=RET.OK, errmsg="收藏成功")



