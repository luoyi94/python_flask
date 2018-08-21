# 进入界面之后展示用户的基本资料(个性签名、昵称、性别)
# 用户修改之后点击保存向服务器发起请求进行数据保存更新

@profile_blue.route("/base_info", methods=["GET", "POST"])
@user_login_data
def base_info():
    user = g.user
    # 展示页面
    if request.method == "GET":
        data = {
            "user_info": user.to_dict() if user else None
        }
        return render_template("news/user_base_info.html", data=data)

    # POST提交为用户要修改信息
    nicke_name = request.json.get("nicke_name")
    signature = request.json.get("signature")
    gender = request.json.get("gender")
    # 设置用户信息
    user.nicke_name = nicke_name
    user.signature = signature
    user.gender = gender
    # 生效
    db.session.commit()
    # 跟新session里面的数据
    session["nicke_name"] = user.nicke_name

    return jsonify(errno = RET.OK, errmsg="修改成功")

