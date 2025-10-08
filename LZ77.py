class Tag:
    def __init__(self, position: int, length: int, nextSymbol: str):
        self.position = position
        self.length = length
        self.nextSymbol = nextSymbol


class LZ77:
    def __init__(self, sequence):
        self.sequence = sequence
        self.windowSize = min(10, len(sequence) // 3)
    
    
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
        tags = list()
        searchWindowStart = -self.windowSize; searchWindowEnd = 0
        lookWindowStart = 0; lookWindowEnd = self.windowSize - 1
        while (lookWindowStart < len(self.sequence)):
            temp = '' 
            for i in range(lookWindowStart, lookWindowEnd+1):
                start = max(0, searchWindowStart); end = max(0, searchWindowEnd)
                matchIndex = self.sequence.find(temp, start, end) if (len(temp)) else -1
                if (i >= len(self.sequence)):
                    break
                if (self.sequence.find(temp + self.sequence[i], start, end) != -1):
                    temp += self.sequence[i]
                    continue
                else : 
                    # Special case for the first occurence of a character
                    if (len(temp) == 0):
                        newTag = Tag(0, 0, self.sequence[i])
                    else :
                        position = lookWindowStart - matchIndex
                        newTag = Tag(position, len(temp), self.sequence[i])
                        
                    advance = len(temp) + 1
                    searchWindowStart += advance; searchWindowEnd += advance
                    lookWindowStart += advance; lookWindowEnd += advance
                    tags.append(newTag) 
                    temp = ""
                    # stop this iteration to search in the next window
                    break
            if (len(temp)) :
                # check if the whole look a head matched the search buffer
                    position = lookWindowStart - matchIndex
                    newTag = Tag(position, len(temp), None if i >= len(self.sequence) else self.sequence[i+1])
                    advance = len(temp) + 1
                    searchWindowStart += advance; searchWindowEnd += advance
                    lookWindowStart += advance; lookWindowEnd += advance
                    tags.append(newTag) 
        
        return tags

    # This method takes a list of tage and returns the original sequence 
    def deCompress(self, tags: list[Tag]) -> str:
        # your implementation 
        pass

    # This method calculates the size after the compression
    def calculateTagsSize(tags: list[Tag]) -> int:
        pass
    