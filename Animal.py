class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.age = new_age

    def set_name(self, new_name = ""):
        self.name = new_name

    def __str__(self):
        return f'Animal {self.name} is {self.age} years old.'

class Dog(Animal):
    def speak(self):
        print("Ham Ham")

    def __str__(self):
        return f'Dog {self.name} is {self.age} years old.'

class Person(Animal):
    id = 1

    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = set()
        self.tag = Person.id
        Person.id += 1

    def __str__(self):
        return f'Person {self.name}, ID = {self.tag} is {self.age} years old.'

    def get_friends(self):
        return self.friends

    def add_friends(self, new_friend):
        if new_friend:
            self.friends.add(new_friend)

    def speak(self):
        print('Hello')


cat = Animal(4)
print(cat)

cat.set_name("Kitty")
print(cat)

print(f'{cat.get_name()} is {cat.get_age()} years old.')

# Poluare obiect cu atribute noi
cat.size = "Big"
print(cat.size)

print('---------------------')

lassie = Dog(10)
lassie.set_name('Lassie')
print(lassie)
lassie.speak()

print('---------------------')
ion = Person('Ion', 21)
maria = Person('Maria', 18)

print(ion)
print(maria)

maria.add_friends("Ion")
maria.add_friends("George")
maria.add_friends("George")

print(maria.get_friends())

maria.speak()





