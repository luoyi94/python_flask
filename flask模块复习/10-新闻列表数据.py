# 新闻列表数据只是当前页面的一部分
# 点击分类时需要去获取当前分类下的新闻数据
# 并在展示的时候需要更新新闻列表界面，不需要整体页面刷新
# 所以新闻数据也使用 ajax 的方式去请求后台接口进行获取

@index_blu.route('/newslist')
def get_news_list():
    """
    获取指定分列的新闻列表
    1，获取参数
    2，校验参数
    3，查询数据
    4，返回数据
    """
    # 1，获取参数
    cid = request.args.get("cid", "1")  # 获取分列id 缺省为1
    page = request.args.get("page", "1")  # 获取页数，默认为第1页
    per_page = request.args.get("per_page", "10")  # 每页多少数据，默认为10条

    # 校验参数
    try:
        cid = int(cid)
        page = int(page)
        per_page = int(per_page)
    except Exception as e:
        current_app.logger.error(e)

    # 查询数据并分页
    filters = []
    # 如果分列id不为1,那么添加分列id进行过滤
    if category_id != "1":
        filters.append(News.category_id == cid)
    try:
        # 按照分列id查询新闻，并按照创建时间字段倒序，返回排序对象
        paginate = News.query.filter(*filters).order_by(News.create_time.desc().paginate(page, per_page, False))
        # 每个页面上面需要展示的数据
        items = paginate.items
        # 获取到总页数
        total_page = paginate.page
        # 当前页面
        current_page = paginate.page

        news_list = []
        for news in items:
            news_list.append(news.to_dict())

        data = {
            # 表示当前页面需要展示的数据
            "news_dict_li": news_list,
            # 表示当前页面
            "current_page": current_page,
            #一共有多少个页面
            "total_page": total_page,
            # 分列
            "cid": cid
        }
        return jsonify(errno=RET.OK, errmsg="ok", data=data)





