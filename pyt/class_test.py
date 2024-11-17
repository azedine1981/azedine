class pre():
    def __init__(self,x):
        print('affichage du carré',lambda x:x*2)
class deux(pre):
    def __init__(self,y):
        print('affichage du cube',lambda x:x*3)
        
obj= deux(5)
print(obj)
