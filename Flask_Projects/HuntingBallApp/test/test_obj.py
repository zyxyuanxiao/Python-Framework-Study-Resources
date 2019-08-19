# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 上午10:40
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_obj.py
# @Software: PyCharm


class Person(object):
    x = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 'weight'

    def talk(self):
        print("person is talking....")

    @classmethod
    def c(cls):
        print('cls-1')


class Chinese(Person):
    x = 2

    def __init__(self, name, age, language):  # 先继承，在重构
        Person.__init__(self, name, age)  # 继承父类的构造方法，也可以写成：super(Chinese,self).__init__(name,age)
        self.language = language  # 定义类的本身属性

    def walk(self):
        print('is walking...')

    @classmethod
    def c(cls):
        print('cls-2')


if __name__ == '__main__':
    pass
    p = Chinese('name', 'age', 'language')
    print(p.x)
    print(p.c())
    print(p.talk())
    print(p.walk())


    class FooParent(object):
        def __init__(self):
            self.parent = 'I\'m the parent.'
            print('Parent')

        def bar(self, message):
            print("%s from Parent" % message)


    class FooChild(FooParent):
        def __init__(self):
            # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），
            # 然后把类B的对象 FooChild 转换为类 FooParent 的对象
            super(FooChild, self).__init__()
            print('Child')

        def bar(self, message):
            super(FooChild, self).bar(message)

            print('Child bar fuction')
            print(self.parent)


    print('_______________________________')
    fooChild = FooChild()
    print('_______________________________')
    fooChild.bar('HelloWorld')
