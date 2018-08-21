@index_blu.route('/')
def index():
    #获取点击排行数据
    new_list = None
    try:
        new_list = News.query.order_by(News.clicks.desc()).limit(constants.CLICK_RANK_MAX_NEWS)
    except Exception as e:
        current_app.logger.error(e)

    click_news_list = []
    for news in new_list if new_list else []:
        click_news_list.append(news.to_basic_dict())

    data = {
        "user_info":user.to_dict() if user else None,
        "click_news_list": click_news_list,
    }

    return render_template("news/index.html", data=data)

