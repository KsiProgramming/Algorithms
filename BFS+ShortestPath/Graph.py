# -----------------------------------------------------------# 
#              BFS + Shortest Path Algorithm                 #
#                                                            #           
#              (C) 2020, LABANI SAID, France                 #
#                                                            #
#               @: labani.said@outlook.com                   #
# -----------------------------------------------------------#
from List   import *
from Vertex import *


class Graph():
    def __init__(self, aGraphName,
                       aVertices,
                       aEdges):
        self.Name       = aGraphName
        self.Vertices   = List[Vertex]([Vertex(vertex) for vertex in aVertices.split(',')])
        self.Edges      = [Edge for Edge in aEdges]
        self.Adj        = {}        
        self.__CreateAdjDict()
        
    def __str__(self):
        return self.Name
    
    def __repr__(self):
        return self.Name
        
            
    def __CreateAdjDict(self):
        for (Vertix,edge) in zip(self.Vertices,self.Edges):
            self.Adj[f"{Vertix}"] = []
            [self.Adj[f"{Vertix}"].append(self.Vertices[edge]) for edge in edge.split(',') if edge !='']
           
    
        

        