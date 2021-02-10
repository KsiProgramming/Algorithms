# -----------------------------------------------------------# 
#              BFS + Shortest Path Algorithm                 #
#                                                            #           
#              (C) 2020, LABANI SAID, France                 #
#                                                            #
#               @: labani.said@outlook.com                   #
# -----------------------------------------------------------#
from Vertex import *

def FindShortestPath(aStartVertex, aTargetVertex):
    def FindPath(aStartVertex, aTargetVertex):
        if aStartVertex == aTargetVertex:
            Path.append(aStartVertex)
        elif aTargetVertex.Predecessor == None:
            Path.append("No path found")
        else :
            FindPath(aStartVertex, aTargetVertex.Predecessor)
            Path.append(aTargetVertex)
        
    Path = []
    FindPath(aStartVertex, aTargetVertex)
    return Path
    
def StringPath(aPathList):    
    return '=>'.join(map(str, aPathList))
    