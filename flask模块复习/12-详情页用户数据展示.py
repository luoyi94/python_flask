
@news_blue.route('/<int:news_id>')
@user_login_data
def news_detail(users_id):

   ## 获取到当前登陆用户的id
   #user_id = session.get("user_id")
   ## 通过id获取用户信息
   #user = None
   #if user_id:
   #    try:
   #        user = User.query.get(user_id)
   #    except Exception as e:
   #        current_app.logger.error(e)

   #data = {
   #    "user_info": user.to_dict() if user else None,
   #}

    return render_template('news/detail.html', data=data)



