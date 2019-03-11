class RangeViaIterator:
    def __init__(self, start, end, step):
        self.start = start - step
        self.end = end - 1
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        self.start += self.step
        if self.start <= self.end:
            return self.start
        else:
            raise StopIteration

#a = RangeViaIterator(1, 59, 10)

#for i in a:
    #print(i)
