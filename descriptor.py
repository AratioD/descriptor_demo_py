"""
A descriptor demo software.
"""


class StringAndNumbers:
    """
    The class Numbers validates all integer based values in the module. 
    Floats are not allowed nor negative integers.
    """

    # https://docs.python.org/3.9/tutorial/classes.html
    # When a class defines an __init__() method,
    # class instantiation automatically invokes __init__()
    # for the newly-created class instance.
    def __init__(self, min_lenght=None):
        self.min_lenght = min_lenght

    # https: // docs.python.org / 3 / reference / datamodel.html
    # object.__set_name__(self, owner, name)
    # Called at the time the owning class owner is created.
    # The descriptor has been assigned to name.
    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    # https://docs.python.org/3/reference/datamodel.html
    # object.__set__(self, instance, value)
    # Called to set the attribute on an instance
    # instance of the owner class to a new value, value.
    def __set__(self, instance, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError(
                    f'ERROR!--> {self.property_name} VALUE NEEDS TO BE POSITIVE INTEGER!'
                )

        elif isinstance(value, str):
            if self.min_lenght is not None and len(value) < self.min_lenght:
                raise ValueError(
                    f'{self.property_name} must be at least {self.min_lenght} characters.'
                )

        else:
            raise ValueError(
                f'ERROR!--> {self.property_name} VALUE NEEDS STRING OR INTEGER'
            )

        instance.__dict__[self.property_name] = value

    # https://docs.python.org/3/reference/datamodel.html
    # Called to get the attribute of the owner class (class attribute access)
    # or of an instance of that class (instance attribute access).
    # The optional owner argument is the owner class,
    # while instance is the instance that the attribute was accessed through,
    # or None when the attribute is accessed through the owner.
    # This method should return the computed attribute value or raise an AttributeError exception.
    # PEP 252 specifies that __get__() is callable with one or two arguments.
    # Python’s own built-in descriptors support this specification; however,
    # it is likely that some third-party tools have descriptors that require both arguments.
    # Python’s own __getattribute__() implementation always passes in both arguments whether they are required or not.
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name, None)


class RegisterNew:
    first_name = StringAndNumbers(2)
    last_name = StringAndNumbers(2)
    price = StringAndNumbers()
    horse_power = StringAndNumbers()
    torque = StringAndNumbers()
    transmission = StringAndNumbers(3)
    consumption = StringAndNumbers(3)


class RegisterOld:
    first_name = StringAndNumbers(2)
    last_name = StringAndNumbers(2)
    price = StringAndNumbers()
    horse_power = StringAndNumbers()
    torque = StringAndNumbers()
    transmission = StringAndNumbers(3)
    consumption = StringAndNumbers(3)


def main():
    p = RegisterNew()
    p1 = RegisterOld()

    try:
        p.first_name = "Jack"
        p.last_name = "Bauer"
        p.price = 200000
        p.horse_power = 1200
        p.torque = 989
        p.transmission = "Automatic"
        p.consumption = "23 Kw/H"
    except ValueError as ex:
        print(ex)

    try:
        p1.first_name = "Mellanie"
        p1.last_name = "Bauer"
        p1.price = 150000
        p1.horse_power = 1044
        p1.torque = 699
        p1.transmission = "Automatic"
        p1.consumption = "39 Kw/H"
    except ValueError as ex:
        print(ex)

    # Memory addresses of "p" object
    print(hex(id(p)))
    print(hex(id(p.first_name)))
    print(hex(id(p.transmission)))

    print("**************************")

    # Memory addresses of "p1" object
    print(hex(id(p1)))
    print(hex(id(p1.first_name)))
    print(hex(id(p1.transmission)))

    print(p.__dict__)
    print(p1.__dict__)
    print(p.__hash__())
    print(p.__class__)
    print(p1.__class__)

    print(p.first_name, " ", p.last_name, " ", p.price, " ", p.horse_power,
          " ", p.torque, " ", p.transmission, " ", p.consumption)

    print(p1.first_name, " ", p1.last_name, " ", p1.price, " ", p1.horse_power,
          " ", p1.torque, " ", p1.transmission, " ", p1.consumption)


# https://docs.python.org/3/library/__main__.html
# __main__ — Top-level script environment
# '__main__' is the name of the scope in which top-level code executes.
# A module’s __name__ is set equal to '__main__' when read from standard input,
# a script, or from an interactive prompt.
if __name__ == '__main__':
    main()
