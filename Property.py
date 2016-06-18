class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.fget is not None:
            return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is not None:
            self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is not None:
            self.fdel(instance)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel)


class Model_property(object):
    def __init__(self):
        self.__temperature = 10

    @Property
    def temperature(self):
        print("Ask temperature")
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        print("New value")
        self.__temperature = value

    @temperature.deleter
    def temperature(self):
        print('goodbye')
        self.__temperature = 0


m = Model_property()
m.temperature = 20
del (m.temperature)
