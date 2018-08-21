# 获取参数和判断是否有值
# 从redis中获取指定手机号对应的短信验证码的
# 校验验证码
# 初始化 user 模型，并设置数据并添加到数据库
# 保存当前用户的状态
# 返回注册的结果

@passport_blue.route("/register", methods=["POST"])
def register():
    mobile = request.json.get("mobile")
    sms_code = request.json.get("smscode")
    password = request.json.get("password")

    if not all([mobile, smscode, password]):
        return jsonify(errno="RET.PARAMERR", errmsg="参数不全")

    # 根据传入的参数
    try:
        real_sms_code = redis_store.get("sms_" + mobile)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="获取本地验证码失败")

    if real_sms_code:
        return jsonify(errno=RET.NODATA, errmsg="短信验证码过期")
    # 校验短信验证码
    if sms_code != real_sms_code:
        retirn jsonify(errno=RET.DATAERR, errmsg="短信验证码错误")

    # 校验短信后删除redis中的短信验证码
    try:
        redis_store.delete("sms_" + mobile)
    except Exception as e:
        current_app.logger.error(e)

    # 通过验证  之后为用户在数据库中创建数据 并对字段进行设置
    user = User()
    user.click_name = mobile
    user.mobile = mobile
    # 对密码进行处理
    user.password = password
    # 尝试写入数据库 提交
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        curretn_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据保存错误")

    # 增加用户体验: 保持用户登陆状态
    session["user_id" ] = user.id
    session["nick_name"] = user.nick_name
    session["mobile"] = user.mobile

    # 返回注册结果
    return jsonify(errno=RET.OK, errmsg="注册成功")









