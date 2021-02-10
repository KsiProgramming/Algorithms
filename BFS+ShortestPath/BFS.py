# -----------------------------------------------------------# 
#              BFS + Shortest Path Algorithm                 #
#                                                            #           
#              (C) 2020, LABANI SAID, France                 #
#                                                            #
#               @: labani.said@outlook.com                   #
# -----------------------------------------------------------#

from Graph import *

def BFS(aGraph, aStartVertex):
    def InitiliazeVertex(aVertex, aDistance):
        aVertex.Color = 'White'
        aVertex.Distance = aDistance
        aVertex.Predecessor = None
        
    def InitializeGraph2BFS(aGraph, aStartVertex):
        for vertex in aGraph.Vertices:
            if vertex != aStartVertex:
                InitiliazeVertex(vertex,None)                
            else:
                InitiliazeVertex(vertex,0)
                
    def UpdateVertexAttributes(aVertex, aPredecessorVertex):
        aVertex.Color = 'Grey'                            
        aVertex.Distance = aPredecessorVertex.Distance + 1
        aVertex.Predecessor = aPredecessorVertex
        
    def UpdateAdjacenciesIfNotVisited(aVertex, aAdjacencies,aQ):
        for Adjacency in aAdjacencies:
            if Adjacency.Color == 'White':
                UpdateVertexAttributes(Adjacency,aVertex)
                aQ.add(Adjacency)
            
    #BFS Main Program  
    InitializeGraph2BFS(aGraph, aStartVertex)
    
    Q = set()
    Q.add(aStartVertex) 
    
    while len(Q) != 0:
        Vertex = Q.pop()
        UpdateAdjacenciesIfNotVisited(Vertex,aGraph.Adj[Vertex.Name],Q)        
        Vertex.Color = 'Black'    
            
