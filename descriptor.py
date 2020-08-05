
class Spec:
    pass

class Pricing:
    pass

class Car:
    pass

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
    


p = Owner()


try:
    p.first_name = "Jack"
    p.last_name = "Bauer"
except ValueError as ex:
    print(ex)
    
    
print(p.first_name, p.last_name)