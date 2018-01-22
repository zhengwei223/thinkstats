# coding=utf-8
# 下面这个是文档说明，hello.__doc__这样就可以获得这个说明
"这是第一个python程序"

# print("大家好")

new_str = "这是一个全局变量"




def hello():
    '''
    这是一个函数
    '''
    return new_str


'''
要执行的代码应该放在程序主体里面
'''
if __name__ == '__main__':
    print(hello())
    print(hello.__doc__)
