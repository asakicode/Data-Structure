class CircularQueue:  # 선형큐의 문제점을 보완하기 위한 원형큐를 제작한다

    def __init__(self, capacity = 50): # 생성자 만들어 줍니다
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0 # 첫 초기 상태
        self.rear = 0  # rear는 마지막 부분 입니다

    def isEmpty(self):
        return self.front == self.rear # front와 rear가 같은 상태임

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity  # d원형 큐라서 고려해야함 모듈레이션을 함

    def  enqueue(self, e): # 스택으로 치면 push
        if not self.isFull(): # 가득 차잇으면 안되니까
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = e
        else:
            print('overflow')

    def dequeue(self): # stack으로 치면 pop
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.queue[self.front]

        else:
            print("underflow")

    def peek(self):  # stack으로 치면 pop
        if not self.isEmpty():
            return self.queue[(self.front + 1) %self.capacity]

        else:
            print("underflow")

    def display(self):
        print('Front: %d, Rear: %d' % (self.front, self.rear))
        i = self.front

        while i !=self.rear:
            i = (i + 1) % self.capacity
            print(f'[{self.queue[i]}]', end=' ')
        print()

    def __str__(self): #연산자 중복 테스트?
        if self.isEmpty():
            return '[]'

        if self.front < self.rear:
            return str(self.queue[self.front+1:self.rear + 1])

        else:
            return str(self.queue[self.front + 1:self.capacity] + \
                       self.queue[0:self.rear + 1])


if __name__ == '__main__':
    Q = CircularQueue(10) # 한바퀴 돌릴려고 10 자리로 만듦
    Q.enqueue('a'); Q.enqueue('b'); Q.enqueue('c');
    Q.enqueue('d'); Q.enqueue('e'); Q.enqueue('f');
    Q.display(); print()

    print('Dequeue --> ', Q.dequeue())
    print('Dequeue --> ', Q.dequeue())
    print('Dequeue --> ', Q.dequeue())
    Q.display(); print()

    Q.enqueue('f'); Q.enqueue('g'); Q.enqueue('h');
    Q.enqueue('i'); Q.enqueue('j');
    print(Q)
