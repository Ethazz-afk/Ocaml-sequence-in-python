# Quand on appelle une fonction qui utilise yield, il faut savoir qu'elle n'est pas
# exécuté. Elle retourne simplement un object generator.
# Et un generator on ne peut le lire qu'une seule fois, il n'est pas stocké dans la mémoire 
class Vide :
    def __init__(self) -> None:
        None


class Noeud: 
    def __init__(self, head , tail) -> None:
        self.head = head
        self.tail = tail



# replace return by yield ! The map funciton creates/returns a generator 
# wich we can use whenever we want !
    
    def map_rec(self, f, seq):
        if seq is Vide :
            return Vide
        return Noeud(f(seq.head), self.map_rec(f, seq.tail))
    
    def map(self, f):
        return Noeud(f(self.head), self.map_rec(f, self.tail))     

    def filter_rec(self, f, seq):
        if seq is Vide:
            return Vide
        if f (seq.head):
            return Noeud(seq.head, self.filter_rec(f, seq.tail))
        return self.filter_rec(f, seq.tail)
    
    def filter(self, f):
        if f(self.head):
            return Noeud(self.head, self.filter_rec(f, self.tail))
        return self.filter_rec(f, self.tail)


    def reduce(self, f):
        res = self.head
        seq = self.tail
        while seq is not Vide:
            res = f(res, seq.head)
            seq = seq.tail
        yield res

    
    def toList(self):
        liste = [self.head]
        seq = self.tail
        while(seq is not Vide):
            liste.append(seq.head)
            seq = seq.tail
        # retourner une liste
        return liste


    def allInt(self, count = 0):
        Noeud(count, self.allInt(count +1))
    
    def display(self):
        print(self.head)
        seq = self.tail
        while seq is not Vide:
            print(seq.head)
            seq = seq.tail

noeud = Noeud(1, Noeud(2, Noeud(3, Noeud(4,Noeud(5,Vide)))))

# noeud2 = noeud.map(lambda a : a*a)
# noeud2.display()

# noeud3 = noeud.filter(lambda a : a % 2 ==0)
# noeud3.display()

# res = noeud.reduce(lambda a,b : a *b )
# print(next(res))
