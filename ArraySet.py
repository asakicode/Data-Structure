class ArraySet:

    def __init__(self,capacity = 50): #생성자 객체
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0  # [수정] self.size로 참조

    def isFull(self):
        return self.size == self.capacity  # [수정] self.capacity로 참조

    def __str__(self):
        return str(self.array[0:self.size])

    def contains(self,e):
        for i in range(self.size):
            if self.array[i] == e:
                return True

        return False

    def insert(self,e):
        if not self.isFull() and not self.contains(e):
            self.array[self.size] = e
            self.size += 1
        else:
            pass

    def delete(self,e):
        for i in range(self.size):
            if self.array[i] == e:
                self.array[i] = self.array[self.size - 1]
                self.size -= 1
                return

    def union(self,setB): #시간 복잡도 O(N) 을 갖게됨 합집합ㅇ인데
        setC = ArraySet()

        for i in range(self.size):
            setC.insert(self.array[i])

        for i in range(setB.size):
            setC.insert(self.array[i])

        return setC

    def intersect(self,setB):
        setC = ArraySet()

        for i in range(self.size):
            if setB.contains(self.array[i]):
                setC.insert(self.array[i])

        return setC

    def difference(self, setB):
        setC = ArraySet()

        for i in range(self.size):
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])

        return setC


if __name__=='__main__':
    S = ArraySet()
    S.insert(10)
    S.insert(20)
    S.insert(30)
    S.insert(40)
    print(S)

    T = ArraySet()
    T.insert(40)
    T.insert(50)
    T.insert(20)
    T.insert(30)
    print(T)

    T.delete(10)
    print(T)

    print(S.union(T))
    print(S.intersect(T))
    print(S.difference(T))
