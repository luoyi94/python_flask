# 在请求根路由时去数据库查询按点击量排行的10条新闻
# 在请求根路由的时候去查询新闻分类，并默认设置第1个分类选中



@index_blu.route("/")
def index():
    # 获取点击排行数据
    news_list = None
    try:
        # 从新闻记录中按照点击倒叙 取固定数量的数据
        news_list = News.query.order_by(News.clicks.desc()).limit(constants.CLICK_RANK_MAX_NEWS)
    except Exception as e:
        current_app.logger.error(e)

    clicke_news_list = []
    # 遍历取出的类比  不存在则为空
    for news in news_list if news_list else []:
        clicke_news_list.append(news.to_basic_dict())

    data = {
        "clicke_news_list" : clicke_news_list
    }

    return render_template("news/index.html", data=data)




