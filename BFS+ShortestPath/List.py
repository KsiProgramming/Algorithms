# -----------------------------------------------------------# 
#              Generic List Template                         #
#                                                            #           
#              (C) 2020, LABANI SAID, France                 #
#                                                            #
#               @: labani.said@outlook.com                   #
# -----------------------------------------------------------#

from typing import TypeVar, Generic

T = TypeVar('T')

class List(Generic[T]):
    def __init__(self, aList=[]) -> None:
        self.Elements: list[T] = aList
        self.__IterList = self.__iter__()

    def Add(self, aElement: T) -> (T,None):
        self.Elements.append(aElement)
        
    def AddRange(self, aElementsList: T) -> (T,None):
        self.Elements.extend(aElementsList)

    def Clear(self)->None:
        self.Elements.clear()
        
    def Insert(self, aIndex, aElement)-> None:
        self.Elements.insert(aIndex, aElement)
    
    def Remove(self, aElement)->None:
        self.Elements.remove(aElement)
        
    def Pop(self) -> T:
        return self.Elements.pop()

    def IsEmpty(self) -> bool:
        return not self.Elements
    
    def Count(self) -> int:
        return self.Elements.__len__()
    
    def __iter__(self) -> T:        
        return self.Elements.__iter__()
    
    def __getitem__(self,aKey) -> T:
        if isinstance(aKey,str):
            if len(aKey.split('=')) >1:
                Key = aKey.split('=')
                try:
                    return self.FindAllOrNone(Key[0],eval(Key[1]))
              
                except:
                    return self.FindAllOrNone(Key[0],Key[1])  
            else:
                try:
                    return self.FindFirstOrNone("Name",aKey)
              
                except:
                    return "The object does not have attribut Name"  


        else:
            return self.Elements.__getitem__(aKey) 
   
    
    def IsCountained(self,aElement) -> T:
        return aElement in self.Elements
    
    def __next__(self) -> T:
        return self.__IterList.__next__()
    
    def __FindElement(self, aAttributeName:str, aAttributeValue)->T:
        return [Element for Element in self.Elements if getattr(Element, aAttributeName)==aAttributeValue]
        
    
    def FindFirstOrNone(self, aAttributeName:str, aAttributeValue)->(T,None):
        SearchResult = self.__FindElement(aAttributeName, aAttributeValue)          
        return SearchResult[0] if len(SearchResult) else None
    
    def FindAllOrNone(self, aAttributeName:str, aAttributeValue)->(T,None):
        SearchResult = self.__FindElement(aAttributeName, aAttributeValue)          
        return SearchResult if len(SearchResult) else None
    
    def Reverse(self):
        self.Elements.reverse()
    
    