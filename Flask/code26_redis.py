import redis


def add_name():
    re = redis.StrictRedis(host="127.0.0.1", port=6379,decode_responses=True)
    result = re.set("name","python")
    print(result)


def get_name():
    re = redis.StrictRedis(host="127.0.0.1",port=6379,decode_responses=True)
    result = re.get("name")
    print(result)


if __name__ == '__main__':
    get_name()

