"""
A descriptor demo software.
"""


class Numbers:
    """
    The class Numbers validates all integer based values in the module. 
    Floats are not allowed nor negative integers.
    """

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(
                f'ERROR!--> {self.property_name} VALUE MUST BE AN INTEGER!')
        if value < 0:
            raise ValueError(
                f'ERROR!--> {self.property_name} VALUE NEEDS TO BE POSITIVE INTEGER!'
            )
        instance.__dict__[self.property_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name, None)


class ValidString:
    """
    The class ValidString validates that all string based values fills defined length and
    there strings are only allowed datatype. 
    """

    def __init__(self, min_lenght=None):
        self.min_lenght = min_lenght

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be a string')
        if self.min_lenght is not None and len(value) < self.min_lenght:
            raise ValueError(
                f'{self.property_name} must be at least {self.min_lenght} characters.'
            )
        instance.__dict__[self.property_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name, None)


class Register:
    first_name = ValidString(2)
    last_name = ValidString(2)
    price = Numbers()
    horse_power = Numbers()
    torque = Numbers()
    transmission = ValidString(3)
    consumption = ValidString(3)


p = Register()
p1 = Register()


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
    p1.horse_power = 788
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

print(p.first_name, " ", p.last_name, " ", p.price, " ", p.horse_power,
      " ", p.torque, " ", p.transmission, " ", p.consumption)
