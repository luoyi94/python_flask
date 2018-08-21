

@index_blue.route('/')
def index():
    # 获取新闻分类
    categories = Category.query.all()
    # 定义列表保存分类数据
    categories_dicts = []

    for category in enumerate(categories):
        # 拼接内容
        categories_dicts.append(category.to_dict())

        data = {
            "categories": categories_dicts
        }

        return render_template('news/index.html', data=data)
