# -----------------------------------------------------------# 
#              BFS + Shortest Path Algorithm                 #
#                                                            #           
#              (C) 2020, LABANI SAID, France                 #
#                                                            #
#               @: labani.said@outlook.com                   #
# -----------------------------------------------------------#

from Graph import *
from BFS   import *


TestGraph = Graph('TestGraph','a,b,c,d,e',['b,c','d,c','d,e','e',''])


BFS(TestGraph,TestGraph.Vertices["a"])


