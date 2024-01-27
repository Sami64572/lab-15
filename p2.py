class CustomLogicMeta(type):
    def __new__(cls, name, bases, dct):
    
        print(f"Creating class: {name}")

        for attr_name, attr_value in dct.items():
            if callable(attr_value):  
                print(f"Injecting custom logic for method: {attr_name}")
                dct[attr_name] = cls.custom_method_wrapper(attr_value)

        new_class = super().__new__(cls, name, bases, dct)

        print(f"Class {name} created")

        return new_class

    @staticmethod
    def custom_method_wrapper(method):
        
        def wrapper(*args, **kwargs):
            print(f"Custom logic before calling method: {method.__name__}")
            result = method(*args, **kwargs)
            print(f"Custom logic after calling method: {method.__name__}")
            return result

        return wrapper

class MyClass(metaclass=CustomLogicMeta):
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")

obj = MyClass(42)

obj.display()
