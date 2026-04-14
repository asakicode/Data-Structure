class PriorityQueue:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size  = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def  enqueue(self, e):
        if not self.isFull():
            self.array[self.size] = e
            self.size += 1

     def findMax(self):
        if self.isEmpty():
            return -1

        highest = 0

        for i in range(1, self.size):
            if self.array[i] > self.array[highest]:
                highest = i
                
        return highest

    def dequeue(self):
        highest = self.findMax()

        if highest != -1:
            self.size -= 1

            self.array[highest], self.array[self.size] = \
                self.array[self.size], self.array[highest]
            return self.array[self.size]



'''이밑에 테스트는 니들이 알아서 하거라'''
''''''
