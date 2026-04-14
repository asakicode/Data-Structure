from linkedList import ListType

class StackType(ListType):
    def __init__(self): #생성자
        super().__init__() # 부모의 것을 상속 받음

    def push(self,e ):
        self.insertFirst(e)

    def pop(self):
        if self.isEmpty():
            print("Empty Stack")
            return None

        return self.deleteFirst()

    def peek(self):
        if self.isEmpty():
            print("Empty Stack")
            return None

        return self.head.data #첫번째 노드의 데이터를 return할게요

    def display(self): #스택에 맞게끔 display 재정의함
        print("Top ->", end="")
        super().display()

if __name__ == "__main__":
    S = StackType()
    S.push('A')
    S.push('B')
    S.push('C')
    S.display()
