class ArrayStack:

    def  __init__(self,capacity = 100): # 생성자 함수
        self.capacity = capacity
        self.stack = [None] * self.capacity
        self.top = -1 #전통적 방식으로 인덱스를 -1 로 해두는 게 좋대요 왜 와이??

    def isEmpty(self): #self는 스택 자신이다.
        return self.top == -1  #true로 리턴

    def isFull(self): #스택이 가득 차 있는지 확인
        return self.top == self.capacity - 1 ## 더이상 빈자리가 없는지 확인한다.

    def push(self,e): #데이터 입력 연산 기능
        if not self.isFull():
            self.top += 1
            self.stack[self.top] = e
        else:
            print('배열이 꽉 찼읍니다.')

    def  pop(self):
        if not self.isEmpty():
             e = self.stack[self.top]
             self.top -= 1
             return e
        else:
            print('배열이 비어있습니다')

    def  peak(self):
        if not self.isEmpty():
             return self.stack[self.top]
        else:
            print('배열이 비어있습니다')

    def display(self):
        for i in range(self.top, -1 , -1):
            print(f'| {self.stack[i]}  |')
            print('-----------')
        print()

    def __str__(self):
        return str(self.stack[0: self.top +1])

if __name__ == "__main__":
    S = ArrayStack(10)

    data = [5,3,8,1,2]

    for d in data:
        S.push(d)

    print(S)


    print(S.pop(),end=' ')
    print(S)

    print(S.peak(),end=' ')
    print(S)
