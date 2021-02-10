# -----------------------------------------------------------# 
#              BFS + Shortest Path Algorithm                 #
#                                                            #           
#              (C) 2020, LABANI SAID, France                 #
#                                                            #
#               @: labani.said@outlook.com                   #
# -----------------------------------------------------------#

class Vertex:
    def __init__(self,  aName=None): 
        self.Name        = aName 
        self.Color       = None
        self.Distance    = 'infinity'
        self.Predecessor = None
    def __str__(self):
        return self.Name
    def __repr__(self):
        return self.Name
    
    
