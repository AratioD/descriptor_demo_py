
class Numbers:
    # def __init__(self, small_int=None):
    #     self.small_int = small_int

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'ERROR!--> {self.property_name} VALUE MUST BE AN INTEGER!')
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
    consuption = ValidString(3)


p = Register()


try:
    p.first_name = "Jack"
    p.last_name = "Bauer"
    p.price = 200000
    p.horse_power = 1200
    p.torque = 989
    p.transmission = "Automatic"
    p.consuption = "23 Kw/H"
except ValueError as ex:
    print(ex)


print(p.first_name, p.last_name, "price-->", p.price, " ", p.horse_power, " ", p.torque, " ", p.transmission, " ", p.consuption)
