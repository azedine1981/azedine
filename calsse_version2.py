class Personne:
    '''la classe des personnes'''
    def __init__(self,nom=None,age=0):
        self.nom=nom
        self.age=age
    def affichage(self):
        print("voici les données personnelels", self.nom, self.age)
#programme principal
p1=Personne('zaki',25)
print(p1.affichage)
