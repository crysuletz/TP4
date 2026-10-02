class Noeud:
    """Représente un nœud d'un arbre d'expression."""
    def __init__(self, val, enfants):    # le constructeur(init)
        self.val= val
        self.enfants= enfants
    
    def ajouter(self, enfant):
        """Ajoute un nœud enfant à la liste des enfants."""
        if isinstance(enfant, Noeud):
            self.enfants.append(enfant)
        
#methode 
# noeud= sa valeur et ses enfants 
# trois= Noeud(3, []) ca donne un noeud 3 avec une liste vide donc sans enfants 
# trois= Noeud(3, (2, mul)) -> la ca marche car on a ecrit self.enfants= enfants , donc il 
# rajoute les enfants dans le noeud 








    