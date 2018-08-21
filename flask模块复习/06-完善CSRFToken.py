# 导入生成csrf_foken 值的函数
from flask_wtf.csrf import generate_csrf
# 调用函数生成csrf_token()
csrf_token = generate_csrf()


@app.after_request
def after_request(response):
    # 调用函数生成csrf_token
    csrf_token = generate_csrf()
    # 通过cookie将值传给前端
    response.set_cookie('csrf_token', csrf_token)
    return response




