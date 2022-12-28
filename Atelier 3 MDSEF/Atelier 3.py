# class rectangle
class Rectangle:

    def __init__(self, longueur, largeur, nom="rectangle"):
        self.longueur = longueur
        self.largeur = largeur
        self.nom = nom

    def surface(self):
        return self.longueur * self.largeur

    def afficher(self):
        print("{ " + self.name + " , longueur: " + str(self.longueur) + " , largeur: " + str(self.largeur) + " }")


# La classe Carré hirté de la classe Rectangle
class Carre(Rectangle):

    def __init__(self, longueur):
        super().__init__(longueur, longueur)
        self.name = "carré"

    def afficher(self):
        print("{ " + self.name + " , longueur: " + str(self.longueur) + " }")

# Une instance de la classe Rectangle
rect = Rectangle(5, 1)
rect.afficher()
print(rect.surface())

# Une instance de la classe Carré
carre = Carre(8)
carre.afficher()
print(carre.surface())

