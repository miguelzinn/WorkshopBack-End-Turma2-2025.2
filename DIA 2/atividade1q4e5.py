class Animal:
    def __init__(self, nome, idade):
          self.nome = nome
          self.idade = idade
    def apresentar(self):
          return f"oi, sou {self.nome} e tenho {self.idade} anos"
    def falar(self):
        pass
class Gato(Animal):
        def __init__(self, nome, idade):
              super().__init__(nome, idade)
        def falar(self):
            return "miau!"
        
class Cachorro(Animal):
       def __init__(self, nome, idade):
             super().__init__(nome, idade)
       def falar(self):
            return "au au!"
       
animais = [Gato("jorge", 2), Cachorro("carlos", 5)]
for Animal in animais:
        print(Animal.apresentar	())
        print(Animal.falar())