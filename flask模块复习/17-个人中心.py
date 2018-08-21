

@profile_blue.route("/info")
@user_login_data
    """
    获取当前用户
    1，获取当前用户登陆的用户模型
    2，返回模型指定的内容
    """
    user = g.user
    if not user:
        # 用户未登陆，重定向到主页
        return redirect("/")

    data = {
        "user_info": user.to_dict(),
    }

    return render_template("news/user.html", data=data)


