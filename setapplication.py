# using the set application

def isSet(setA):
    if isinstance(setA, (set)):
        pass
    else:
        raise ValueError

class MySet:
    def __init__(self, setA, setB):
        isSet(setA)
        isSet(setB)
        setA = self.setA
        setB = self.setB
        self.setUnion = set([])
        self.setIntersection = set([])
        self.setDifference = set([])
        self.copyset = set([])
    
    def union(self, setA, setB):
        self.setUnion = setA | setB
        return self.setUnion
    
    def intersection(self, setA, setB):
        self.setIntersection= setA & setB
        return self.setIntersection
    
    def setDifference(self, setA, setB):
        self.setDiff = setA - setB
        return self.setDiff

    def subset(self, setA, setB):
        return setA.issubset(setB)
    def superset(self, setA, setB):
        return setA.issuperset(setB)

    def symmetrical_difference(self, setA, setB):
        return setA.symmetrical_difference(setB)

    def copy_set(self, setA):
        self.copy_set = setA.copy()
        return self.copy_set
