'''题目：模仿静态变量的用法。'''
#  借鉴这篇文章 https://blog.csdn.net/dawnranger/article/details/78306878


# solution 1
class Foo(object):
    _count = 0  # 不直接操作这个变量，也避免访问它

    @property
    def count(self):
        return Foo._count

    @count.setter
    def count(self, num):
        Foo._count = num


f1 = Foo()
f2 = Foo()

print(f1.count, f1._count, f2.count, f2._count)

f1.count = 1
print(f1.count, f1._count, f2.count, f2._count)


# solution 2
class Foo(object):
    __count = 0  # 不直接操作这个变量，也避免访问它

    @classmethod
    def get_count(cls):
        return cls.__count

    @classmethod
    def set_count(cls, num):
        Foo.__count = num


f1 = Foo()
f2 = Foo()
Foo.set_count(1)
print(f1.get_count(), f2.get_count())
