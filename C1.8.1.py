class Dog:
    name, breed, gender, age = None, None, None, None
    def __init__(self, name, breed, gender, age):
        self.name = name
        self.breed = breed
        self.gender = gender
        self.age = age


    def print(self):
        print("=^.^=___=^.^=")
        print("Имя =", self.name)
        print("Порода =", self.breed)
        print("Пол =", self.gender)
        print("Возраст =", self.age)

    def get_name(self):
        return self.name

    def get_breed(self):
        return self.breed

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

dog1 = Dog("Феликс", "Собака", "Мальчик", "2")
dog1.print()