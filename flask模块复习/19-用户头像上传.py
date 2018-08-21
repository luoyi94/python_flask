# 用户可以进行头像的修改，上传完毕之后更新个人中心跟头像相关的标签内容
# 上传的头像文件保存到【七牛云】提供的文件存储服务器中

@profile_blu.route("/pic_info", methods=["GET", "POST"])
@user_login_data
def pic_info():
    user = g.user
    # GET请求则为展示静态页面
    if request.methods == "GET":
        data = { "user_info":user.to_dict() if user else None }
        return render_template("news/user_pic_info.html", data=data)

    # POST提交头像数据
    # 获取头像文件
    avatar = request.files.get("avatar").read()
    # 调用第三方接口上传  返回url
    url = storage(avatar)

    # 设置用户模型相关数据
    user.avatar_url = url
    # 将数据保存到数据库
    db.session.commit()

    data = {
        "avatar_url": constants.QINIU_DOMIN_PREFIX + url
    }

    return jsonify(errno=RET.OK, errmsg="上传成功", data=data)
