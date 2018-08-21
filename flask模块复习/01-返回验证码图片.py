from . import passport_blue
from info.utils.captcha.captcha import captcha





@passport_blue.route("/image_code")
def image_code():

	# 获取前端提交过来的uuid 通过链接?/code_id="内容"
	code_id = request.arge.get("code_id")

	if not code_id:
		return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

	# 第三方提供的为 图片验证码名字 验证码内容 验证码图片
	name, text, image = captcha.generate_captcha()

	# 第一个参数为name, key, value, ex过期时间
	redis_store.set("sms_code" + code_id, code_id, text, 300)

	resp = make_response(image)

	return "resp"


