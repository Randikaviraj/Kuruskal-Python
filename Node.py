class Node:
    def __init__(self,parent:int):
        self.rank = 0
        self.parent = parent
        
    def setRank(self,value:int):
        self.rank=value
        
    def setParent(self,value:int):
        self.parent=value  
        
    def getRank(self):
        return self.rank
    
    def getParent(self):
        return self.parent