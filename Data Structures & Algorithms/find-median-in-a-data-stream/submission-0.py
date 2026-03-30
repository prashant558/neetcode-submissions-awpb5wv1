class MedianFinder:

    def __init__(self):
        self.arr =[]

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        n = len(self.arr)
        arr = sorted(self.arr)
        if n % 2 == 0:
            return (arr[n//2] + arr[((n+1)//2)-1])/2
        else:
            return arr[((n+1)//2)-1]
        
        