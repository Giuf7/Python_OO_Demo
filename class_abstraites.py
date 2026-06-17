"""
Boutons, étiquettes, champs de texte, tableaux
https://www.youtube.com/watch?v=zY4WnyEV_Ao&t=120s
"""

from abc import ABC, abstractmethod

# Interface
class Widget(ABC):
    def test(self):
        print('test !')

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def command(self):
        pass

    @abstractmethod
    def pack(self):
        pass

# w = Widget()
# w.test()

class Button(Widget):
    def render(self):
        print("Rendu d'un bouton")

class Label(Widget):
    def render(self):
        print("Rendu d'une étiquette")

class TextField(Widget):
    def test(self):
        print("Test d'un champ de texte")

    def render(self):
        print("Rendu d'un champ de texte")

class Table(Widget):
    def render(self):
        print("Rendu d'un tableau")

btn = Button()
btn.test()
btn.render()

txf = TextField()
txf.test()
txf.render()