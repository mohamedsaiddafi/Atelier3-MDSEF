class Vecteur2D:
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

    # La méthode afficher()
    def afficher(self):
        return "(" + str(self.x) + ", "+ str(self.y) + ")"
    
    # Méthode de surcharge d'addition de deux vecteurs du plan
    def __add__(self, vecteur2D):
        return Vecteur2D(self.x + vecteur2D.x, self.y + vecteur2D.y)


# Un vecteur 2D sans paramètre
vect1 = Vecteur2D()

# Un vecteur 2D avec ses deux paramètre
vect2 = Vecteur2D(2,4)

# Affichage des vecteurs comme un tuple
print(vect1)
print(vect2)

# Affichage des vecteurs avec la méthode afficher()
print(vect1.afficher())

# La somme de deux vecteurs du plan
vect3 = vect1 + vect2

# L'affichage de la somme de deux vecteurs du plan
print(vect3.afficher())