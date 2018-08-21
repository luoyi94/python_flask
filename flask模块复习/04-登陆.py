# 获取参数和判断是否有值
# 从数据库查询出指定的用户
# 校验密码
# 保存用户登录状态
# 返回结果

@passport_blue.route("/login", methods=["POST"])
def login():
    mobile = request.json.get("mobile")
    password = request.json.get("password")

    if not all([mobile, passowrd]):
        return jsonify(errno=RET.PARAMERR,errmsg="参数错误")

    # 从数据库查询出指定的用户
    try:
        user = User.query.filter_by(mobile=mobile).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="查询错误")

    if not user:
        return jsonify(errno=RET.USERERR, errmsg="用户不存在")

    # 判断用户密码是否正确
    if not user.check_password(passowrd):
        return jsonify(errno=RET.PWDERR, errmsg="密码错误")

    # 保存用户登陆状态
    session["user_id"] = user.id
    session["nick_name"] = user.nick_name
    session["mobile"] = user.mobile
    # 记录用户最后一次登陆时间，做登陆状态保持的时间
    user.last_login = datetime.now()

    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
    return jsonify(errno=RET.OK, errmsg="登陆成功")

