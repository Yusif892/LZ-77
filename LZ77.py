class Tag:
    def __init__(self, position: int, length: int, nextSymbol: str):
        self.position = position
        self.length = length
        self.nextSymbol = nextSymbol


class LZ77:
    def __init__(self,sequence, windowSize: int = 10):
        self.windowSize = windowSize
        self.sequence = sequence
    
    
    # This method searches the look ahead window to find the longest match
    # starts form position @start, ends at the match ends or at the end of the window 
    # returns the position where the match stops 
    def findLongestMatch(self, start: int) -> int:
        end = len(self.sequence)
        searchBegin = max(0,start-self.windowSize)
        
        searchBuffer = self.sequence[searchBegin:start]
        lookAhead = self.sequence[start:end]
        
        bestLength = 0
        bestIndex = start
        
        for i in range(len(searchBuffer)):
            length = 0
            while(i+length < length(searchBuffer) and 
                  length < len(lookAhead) and
                  searchBuffer[i+length] == lookAhead[length]):
                length +=1
        
        if length > bestLength:
            bestLength =length
            bestIndex = start + length - 1        
            
        return bestIndex
            

    # This method takes a string sequence and returns a list of tags 
    def compress(self) -> list[Tag]:
        # your implementation 
        pass
    
    # This method takes a list of tage and returns the original sequence 
    def deCompress(self, tags: list[Tag]) -> str:
        # your implementation 
        pass

    # This method calculates the size after the compression
    def calculateTagsSize(tags: list[Tag]) -> int:
        pass
