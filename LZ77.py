class Tag:
    def __init__(self, position: int, length: int, nextSymbol: str):
        self.position = position
        self.length = length
        self.nextSymbol = nextSymbol


class LZ77:
    def __init__(self, windowSize: int):
        self.windowSize = windowSize
    
    # This method takes a string sequence and returns a list of tags 
    def compress(self, sequence: str) -> list[Tag]:
        # your implementation 
        pass

    # This method takes a list of tage and returns the original sequence 
    def deCompress(self, sequence: list[Tag]) -> str:
        # your implementation 
        pass

    # This method calculates the size after the compression
    def calculateTagsSize(tags: list[Tag]) -> int:
        pass
