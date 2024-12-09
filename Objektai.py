# class Human(): # klases deklaracija
#     def __init__(self, name): # init - Konstruktorius
#         self.vardas = name
#     def __str__(self): # str - dunder/magic metodas | self - tai kreipinys pats i save kai sukurtas objektas |  self = pirmas_zmogus 
#         return self.vardas # return pirmas_zmogus.vardas
#     def dainuoti(self):
#         print("As dainuoju")
    

# pirmas_zmogus = Human("Justas") # pasleptai iskvieciamas __init__

# # print(Human.__str__(pirmas_zmogus))
# print(pirmas_zmogus.__str__()) # self automatiskai = objektas.str(objektas)

# antras_zmogus = Human("Jonas") # pasleptai iskvieciamas __init__

# antras_zmogus.dainuoti()


# class Preke():
#     def __init__(self):
#         self.kaina = 50

# class Nuolaida():
#     def __init__(self, item):
#         self.preke = item
#     def taikyti_nuolaida(self):
#         self.preke.kaina  = self.preke.kaina * 0.8


# saldainis = Preke()

# nuolaida_saldainiams = Nuolaida(saldainis)



# class Animal():
#     def __init__(self, amzius):
#         self.age = amzius

#     def __str__(self):
#         return str(self.age)

# class Cat(Animal):
#     def __init__(self, amzius, spalva):
#         super().__init__(amzius) # Animal.__init(amzius)
#         self.color = spalva

#     def __str__(self):
#         result = f"{super().__str__()} {self.color}"
#         return result


# gyvunas = Animal(5)
# print(gyvunas)

# kate = Cat(4,"Juoda")

# print(kate)


# class Animal():
#     def __init__(self, amzius):
#         self.age = amzius

#     def __str__(self):
#         return str(self.age)
#     def kalbeti(self):
#         print("How do I talk ?")

# class Cat(Animal):
#     def __init__(self, amzius, spalva):
#         super().__init__(amzius) # Animal.__init(amzius)
#         self.color = spalva

#     def __str__(self):
#         result = f"Cat is {super().__str__()} old  and {self.color} color"
#         return result
#     def catch_mouse(self):
#         print("I am trying to catch a mouse")
#         # print(".....")
#         # print("Got one!")


# class Dog(Animal):
#     def __init__(self, amzius, spalva):
#         super().__init__(amzius) # Animal.__init(amzius)
#         self.color = spalva

#     def __str__(self):
#         result = f"Dog is {super().__str__()} old  and {self.color} color"
#         return result
#     def kalbeti(self):
#         print("Au au")


# gyvunas = Animal(5)

# kate = Cat(4,"Black")
# dog = Dog(2,"Grey")

# animals = [gyvunas,kate,dog]

# for animal in animals:
#     # print(animal)
#     if isinstance(animal,Animal): # isInstance atsizvelgia i paveldejima | Sitas naudojamas dazniau ir korektiskesnis
#         animal.kalbeti()
#     # if type(animal) is Animal: # type ir is neatsizvelgia
#     #     animal.kalbeti()
#     if isinstance(animal,Cat):
#         animal.catch_mouse()

