import math
class Tag:
    def __init__(self, position: int, length: int, nextSymbol: str):
        self.position = position
        self.length = length
        self.nextSymbol = nextSymbol


class LZ77:
    def __init__(self, sequence):
        self.sequence = sequence
        # self.windowSize = min(10, len(sequence) // 3)
        self.windowSize = 10
    
    
    # This method searches the look ahead window to find the longest match
    # starts form position @start, ends at the match ends or at the end of the window 
    # returns the position where the match stops 
    def findLongestMatch(self,sub:str, start: int, end: int) -> int:
        longestMatch = 0
        while(start+1 <= end):
            temp = self.sequence[start] + self.sequence[start+1]
            if (temp == sub):
                longestMatch += 2
                start += 2
            else :
                break
        return longestMatch

            

    
    
    # This method takes a string sequence and returns a list of tags 
    def compress(self) -> list[Tag]:
        tags = list()
        searchWindowStart = -self.windowSize; searchWindowEnd = 0
        lookWindowStart = 0; lookWindowEnd = self.windowSize - 1
        while (lookWindowStart < len(self.sequence)):
            temp = ''   
            longestMatch = 0
            if (lookWindowStart + 1 < lookWindowEnd and lookWindowEnd > 2):
                if (self.sequence[lookWindowStart:lookWindowStart+2] == self.sequence[lookWindowStart-2:lookWindowStart]):
                    longestMatch = self.findLongestMatch(self.sequence[lookWindowStart:lookWindowStart+2],lookWindowStart, min(lookWindowEnd, len(self.sequence))-1)
            
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
                        advance = 1
                    else :
                        if (len(temp) >= longestMatch):
                            position = lookWindowStart - matchIndex
                            newTag = Tag(position, len(temp), self.sequence[i])
                            advance = len(temp) + 1
                        else:
                            newTag = Tag(2, longestMatch, "" if lookWindowStart + longestMatch >= len(self.sequence) else self.sequence[lookWindowStart + longestMatch])
                            advance = longestMatch + 1
                        
                    searchWindowStart += advance; searchWindowEnd += advance
                    lookWindowStart += advance; lookWindowEnd += advance
                    tags.append(newTag) 
                    temp = ""
                    lookWindowStart = min(lookWindowStart, len(self.sequence)); lookWindowEnd = min(lookWindowEnd, len(self.sequence))
                    # stop this iteration to search in the next window
                    break
            if (len(temp)) :
                # check if the whole look a head matched the search buffer
                    position = lookWindowStart - matchIndex
                    newTag = Tag(position, len(temp), "" if i + 1>= len(self.sequence) else self.sequence[i+1])
                    advance = len(temp) + 1
                    searchWindowStart += advance; searchWindowEnd += advance
                    lookWindowStart += advance; lookWindowEnd += advance
                    tags.append(newTag) 
        
        return tags

    # This method takes a list of tage and returns the original sequence 
    def deCompress(self, tags: list[Tag]) -> str:
        Data = []

        for tag in tags:
            start = len(Data) - tag.position
            for i in range(tag.length):
                Data.append(Data[start + i])

            if tag.nextSymbol != '':
                Data.append(tag.nextSymbol)

        return ''.join(Data)

    # This method calculates the size after the compression
    def calculateTagsSize(self, tags: list[Tag]) -> int:
        if not tags:
            return 0
        max_pos = max(tag.position for tag in tags)
        max_len = max(tag.length for tag in tags)
        
        if max_pos == 0:
            pos_bits = 1
        else:
            pos_bits = math.floor(math.log2(max_pos)) + 1
        if max_len == 0:
            len_bits = 1
        else:
            len_bits = math.floor(math.log2(max_len)) + 1

        symbol_bits = 8

        return pos_bits + len_bits + symbol_bits
    