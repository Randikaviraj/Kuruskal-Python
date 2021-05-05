from Node import Node

class Graph:
    def __init__(self,noOfVertices) -> None:
        self.verticeSet=[]
        for i in range(noOfVertices):
            self.verticeSet.append(Node(i))  
        self.graph=[]
        
    def addEdgeToGraph(self,value: list):
        self.graph.append(value)
        
    def sortGraph(self):
        def keyFunc(list):
            return list[2]
        self.graph.sort(key=keyFunc)
        
    def find(self,vertice)-> int:
        return self.verticeSet[vertice].getParent()
    
    def union(self,vertice1,vertice2)-> bool:
        parent1=self.find(vertice1)
        parent2=self.find(vertice2)
        if parent1==parent2:
            return False
        if self.verticeSet[parent1].getRank() > self.verticeSet[parent2].getRank():
            self.verticeSet[vertice2].setParent(parent1)
            for i in range(len(self.verticeSet)):
                if self.verticeSet[i].getParent()==parent2:
                    self.verticeSet[i].setParent(parent1)     
        elif self.verticeSet[parent1].getRank() < self.verticeSet[parent2].getRank():
            self.verticeSet[vertice1].setParent(parent2)
            for i in range(len(self.verticeSet)):
                if self.verticeSet[i].getParent()==parent1:
                    self.verticeSet[i].setParent(parent2)  
        else :
            self.verticeSet[vertice2].setParent(parent1)
            self.verticeSet[parent1].setRank(self.verticeSet[parent2].getRank()+1)
            for i in range(len(self.verticeSet)):
                if self.verticeSet[i].getParent()==parent2:
                    self.verticeSet[i].setParent(parent1)
        return True 
             
    def getGraph(self):
        return self.graph
    
 