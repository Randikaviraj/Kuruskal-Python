from Graph import Graph
import sys
import time

      
        
def kuruskalAlgorithm(g: Graph):
    minimumSpanningTree=[]
    g.sortGraph()
    for edge in g.getGraph():
        if g.union(edge[0],edge[1]):
            minimumSpanningTree.append(edge)
        
    return minimumSpanningTree    


if __name__ =="__main__":
    try:

        with open(sys.argv[1],"r") as file:
            print(f"{sys.argv[1]} Reading..")
            line=file.readline()
            noOfVertices=line.split(" ")[1]
            g=Graph(int(noOfVertices))
            line=file.readline()
            while line:
                edge=[]
                list=line.split(" ")
                for val in list:
                    val=val.strip('\n')
                    if val:
                        edge.append(int(val))
                g.addEdgeToGraph(edge)
                line=file.readline()
                
            print('Algorithm Started::')
            seconds = time.time()
            l=kuruskalAlgorithm(g)
            seconds = seconds-time.time()
            for edge in l:
                print(str(edge[0])+" - "+str(edge[1])+" weight is "+str(edge[2]))
            print('Finished::')
            print('Running Time in second'+str(seconds))
            
    except Exception as e:
        print(e)
        print('Invalid no of Arguments :: python Kuruskal.py  <filename> ')