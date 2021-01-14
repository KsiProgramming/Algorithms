# -----------------------------------------------------------# 
#                   MergeSort Algorithm                      #
#                                                            #           
#              (C) 2020, LABANI SAID, France                 #
#                                                            #
#               @: labani.said@outlook.com                   #
# -----------------------------------------------------------#


def MergeSort(aArray):
    """
    Parameters
    ----------
                aArray : List
                            Array list of numbers or letters.
    Returns
    -------
                List
                    Sorted list of the list argument.
    """
    
    def HalfingSearchSpace(aList):
        """     
        Parameters
        ----------
                    aList : List
                            Array list of numbers or letters.

        Returns
        -------
                List
                    Break the list two sub lists (Halfing).

        """
        if len(aList) <= 1:
            return aList 
        
        MidList = len(aList)//2
        return SortMerge(HalfingSearchSpace(aList[:MidList])
                        ,HalfingSearchSpace(aList[MidList:]))
    
    def SortMerge(aHalfLeft,aHalfRight): 
        """
        Parameters
        ----------
        aHalfLeft : List
            List of numbers or letters.
        aHalfRight : List
            List of numbers or letters.

        Returns
        -------
        MergingList : List
            After sorting and merging the two lists in MergingList.

        """
        MergingList = []
        LeftIndex = RightIndex = 0
        while LeftIndex < len(aHalfLeft) and RightIndex < len(aHalfRight):
            if aHalfLeft[LeftIndex] < aHalfRight[RightIndex]:
                MergingList.append(aHalfLeft[LeftIndex])
                LeftIndex += 1
            else:
                MergingList.append(aHalfRight[RightIndex])
                RightIndex += 1
        MergingList += aHalfLeft[LeftIndex:] +aHalfRight[RightIndex:]        
        return MergingList
    
    #Main Program Call    
    return HalfingSearchSpace(aArray)
        









