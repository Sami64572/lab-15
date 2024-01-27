class LoggingMixin:
    def log(self, message):
        print(f"[Log] {message}")

class SerializationMixin:
    def serialize(self):
        return str(self.__dict__)

class Person(LoggingMixin, SerializationMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)


person.log("This is a log message.")

serialized_data = person.serialize()
print(f"Serialized Data: {serialized_data}")