class Personne():
    """une class qui définit les personnes"""
    def __init__(self,nom,age,genre):
        self.nom=nom
        self.age=age
        self.genre=genre
    def affichage(self):
        print("Bonjour {0} vous avez {1}".format(self.nom,self.age))

class Eleve(Personne):
    def __init__(self,Nom,classe,note):
        Personne.__init__(self,Nom,age,genre)
        self.classe=classe
        self.genre=genre
              
if __name__=="__main__":
              p1=Personne('Ahmed',24,'M')
              p2=Personne('Fatima',30,'F')
              p1.affichage()
              p2.affichage()
              p3=Eleve('karim',13,'M')
              p3.affichage()
