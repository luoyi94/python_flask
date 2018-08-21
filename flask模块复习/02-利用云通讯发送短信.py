# 发送短信验证码实现流程：
#   接收前端发送过来的请求参数
#   检查参数是否已经全部传过来
#   判断手机号格式是否正确
#   检查图片验证码是否正确，若不正确，则返回
#   删除图片验证码
#   生成随机的短信验证码
#   使用第三方SDK发送短信验证码

@ passport_blue.route("/sms_code", methods=["POST"])
def  sms_code():
    print("前端发送的地址= " + request.url)
    # 手机号码
    mobile = request.json.get("mobile")
    # 输入图片验证码的内容  接收用户输入的参数
    image_code = request.json.get("image_code")
    # 图片验证码的编号  用与在数据库进行校验
    image_code_id = request.json.get("image_code_id")
    # 判断参数是否为空
    if not all([mobile, image_code, image_code_id]):
        return jsonify(errno = RET.PARAMERR, errmsg="参数不全")
    # 校验手机号码是否正确    是否合法
    if not re.match("^1[3578][0-9]{9}$", mobile):
        return jsonify(errno=RET.DATAERR, errmsg="手机号码不正确")
    # 检查手机号码图片验证码是否正确
    try:
        # 根据图片id查询redis中存入的图片uuid
        real_image_code = redis_store.get("sms_code_" + image_code_id)
        if real_image_code:
            # 如果有值，则删除redis缓存中的内容
            real_image_code = real_image_code.decode()
            redis_store.delete("ImageCode_" + image_code_id)

    if image_code_id:
        # 判断验证码是否过期
        return jsonify(errno=RET.NODATA, errmsg="图片验证码过期")

    # 进行验证码内容的对比  用户输入的= ? 根据id从数据库中查询到的
    if image_code().lower() != real_image_code.lower():
        return jsonify(errno="RET.DATAERR", errmsg="验证码输入错误")

    # 判断手机号码是否已经注册
    try:
        # 将传入的手机号码在数据库中进行过滤查询
        # 返回第一个结果，进行判断是否存在
        user = User.query.filter_by(mobile=mobile).first()
    except Exception as e:
        # 存入日志
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库查询错误")
    if user:
        return jsonify(errno="RET.DATAEXIST", errmsg="手机号码已经被注册")
    # 生成随机的验证码
    result = random.randint(0, 999999)
    # 保证为6位
    sms_code = "%06d" % result
    # 第三方模块发送短信
    current_app.logger.debug("短信验证码内容：%s" % sms_code)
    result =  CCP().send_template_sms(mobile, [sms_code, constants.SMS_CODE_REDIS_EXPIRES / 60], "1")

    if result != 0:
        return jsonify(errno=RET.THIRDERR, errmsg="发送短信失败")

    # 保存短信内容到redis中
    try:
        redis_store.set("sms_" + mobile, sms_code, constants.SMS_CODE_REDIS_EXPIRES)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="保存短信验证码失败")

    return jsonify(errno=RET.OK, errmsg="发送成功")


