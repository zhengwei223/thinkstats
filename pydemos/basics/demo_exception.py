# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except ValueError as e:
        print("参数没有包含数字{0}\n".format(e))


class MyException(Exception):
    pass


try:
    raise MyException("这是我自己定义的异常")
except:
    print("catch you")

# 调用函数
# temp_convert("xyz");
