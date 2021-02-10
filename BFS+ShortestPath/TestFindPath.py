# -----------------------------------------------------------# 
#              BFS + Shortest Path Algorithm                 #
#                                                            #           
#              (C) 2020, LABANI SAID, France                 #
#                                                            #
#               @: labani.said@outlook.com                   #
# -----------------------------------------------------------#



from Graph            import *
from BFS              import *
from FindShortestPath import *


#Building The Graph Object
GraphTest = Graph('TestGraph','a,b,c,d,e',['b,c','d,c','d,e','e',''])

#Creating the BFS Graph (Launching The BFS Algorithm)
BFS(GraphTest,GraphTest.Vertices["a"])
        
#Finding the shortest path from noed "a" to noeud "e"       
ShortestPath = FindShortestPath(GraphTest.Vertices["a"], GraphTest.Vertices["e"])

#Printing The Shortest Path
print(StringPath(ShortestPath))

