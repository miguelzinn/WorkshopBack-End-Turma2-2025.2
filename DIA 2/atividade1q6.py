class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"{self.nome}, {self.idade} anos"

    def falar(self):
        pass

class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar(self):
        return "Miau!"

class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar(self):
        return "Au au!"
    
class Zoologico:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def listar_animais(self):
        return [f"{a.apresentar()} → {a.falar()}" for a in self.animais]

    def filtrar_por_tipo(self, tipo):
        return [a for a in self.animais if isinstance(a, tipo)]

