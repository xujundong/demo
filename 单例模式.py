#确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例，这个类称为单例类，单例模式是一种对象创建型模式。
class Singleton:
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance=object.__new__(cls)
        return cls.__instance

a=Singleton()
b=Singleton()
print(id(a))
print(id(b))