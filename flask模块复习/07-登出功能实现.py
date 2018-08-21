@passport_blue.route("/logout", methods=["POST"])
def logout():
    """
    清楚session中的对应登陆之后保存的信息
    """
    session.pop('user_id', None)
    session.pop('nick_name', None)
    session.pop('mobile', None)

    return jsonify(errno=RET.OK, errmesg='OK')





