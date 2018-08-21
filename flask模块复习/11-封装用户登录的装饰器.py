import functools


def user_login_data(f):
    @functools.wraps(f)
    def wrapper(*args, *kwargs):
        user_id = session.get("user_id")
        # 默认值
        user = None
        if user_id:
            # 根据id查询当前用户
            user = User.query.get(user_id)
        g.user = user
        return f(*args, *kwargs)
    return wrapper



