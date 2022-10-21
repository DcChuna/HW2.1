na = input('dog age')
nas = input('dog name')


class dog:
    def __init__(self,name , age):
        self.name = name
        self.age = age


    def dog_age(self):
        global nas
        if nas == 1:
            na == 15
            print(nas)
        if nas == 2:
            na == 24
            print(nas)
        if nas == 3:
            print(nas)
            na == 28
        if nas == 4:
            na == 32
            print(nas)
        if na != 4:
            print(int(na * 4 - 4 + 32))
            print(nas)


dog1 = dog(
    nas,
    na
)
print(dog1.dog_age())
