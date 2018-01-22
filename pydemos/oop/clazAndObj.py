# coding=utf-8


class Car(object):

    # 构造方法
    def __init__(self, wheelNum, color):
        self.wheelNum = wheelNum
        self.color = color

    def info(self):
        return "Car's info:wheelnum {0},coloe {1}".format(self.wheelNum, self.color)


class A(object):
    def __init__(self):
        print("A.__init__")


class SaloonCar(Car, A):

    def __init__(self, wheelNum, color, brand):
        # print(self.__class__.mro())
        # 调用父类构造器
        super(Car, self).__init__()
        self.brand = brand

    # 方法重写
    def info(self):
        # 调用父类方法
        return super().info() + ",brand {0}".format(self.brand)


# # 构造器初始化属性
# car1 = Car(4, 'red')
# print(car1.color)
# # 更改属性
# car1.color = 'yellow'
# print(car1.color)

bmw = SaloonCar(4, 'red', 'bmw')
print(bmw.info())
