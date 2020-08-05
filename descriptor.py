
class Spec:
    pass

class Pricing:
    pass

class Car:
    pass

class Numbers:
    def __init__(self, small_int=None):
        self.small_int = small_int

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'{self.property_name} must be a integer')
        if self.small_int is not None and self.small_int > 0:
            raise ValueError(
                f'{self.property_name} must be at least {self.small_int} characters.'
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
    

class Owner:
    first_name = ValidString(3)
    last_name = ValidString(3)
    price = Numbers(0)
    


p = Owner()


try:
    p.first_name = "Jack"
    p.last_name = "Bauer"
    p.price(3)
except ValueError as ex:
    print(ex)
    
    
print(p.first_name, p.last_name)