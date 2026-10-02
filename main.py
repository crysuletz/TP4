#exp(2+y) - les enfants de exp sont le + et ses enfants ( 2 et y )

from noeud import Noeud

y= Noeud(val="y", enfants=())
deux= Noeud(val=2, enfants=())

plus=Noeud(val="+", enfants=(deux, y))

exp= Noeud(val="exp", enfants="plus")
exp.afficher()
# affichage polonais = affiche chaque noeud dans l ordre
# donc par exemple ecouter vocal tp3 iphone
#dans programme principal
#valeur="exp"
#enfants = plus meme chose que ajouter enfant plus

def afficher(self): #on veut afficher l objet
    print(self.val)

#on connait pas y dcp on a besoin de y on utilise un dict 