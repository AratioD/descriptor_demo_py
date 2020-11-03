"""
A descriptor demo software.
"""


class StringAndNumbers:
    """
    The class Numbers validates all integer based values in the module. 
    Floats are not allowed nor negative integers.
    """
    def __init__(self, min_lenght=None):
        self.min_lenght = min_lenght

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

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
