# 使用原密码和新密码进行密码修改

@profile_blue.route("/pass_info", methods=["GET", "POST"])
@user_login_data
def pass_info():
    # GET请求为展示修改页面
    if request.methods == "GET":
        return render_template("news/user_pass_info.html")
    # POST提交修改密码
    user = g.user
    old_password = request.json.get("old_password")
    new_password = request.json.get("new_password")
    # 校验
    if not all([old_password, new_password]):
        return jsonify(errno=RET.PARAMERR, errmsg="请输入密码")

    # 判断旧密码是否正确，只有旧密码正确才能修改密码
    if not user.check_password(old_password):
        return jsonify(errno=RET.PARAMERR, errmsg="旧密码错误")

    # 如果旧密码正确，直接更新到当前的数据库中
    user.password = new_password
    db.session.commit()
    return jsonify(errno=RET.OK, errmsg= "修改密码成功")


