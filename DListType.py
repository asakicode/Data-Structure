from platform import node


class Node: # 어린이를 표현하기 위한 클래스
    def __init__(self, data=None, prev = None, next = None): #어린이가 나가기위해선 data라는 이름표, next라는 허리끈
        self.data = data
        self.prev = prev # 하나가 더 생겼네??
        self.next = next


class DListType: # linkedList의 헤드포인터와 헤드 노드의 개념이 조금 다름, 이거 이해해봐야함
    def __init__(self):
        self.H = Node() # H 어린이 즉 노드
        self.T = Node() # T 어린이 노드를 만들었다 -> Node에서 data를 None이라고 일단 설저했으므로 데이터의 이름이 없을 수 있다.

        self.H.next = self.T  # 맨 앞 어린이 즉 H 가 잡고 있는 녀석은 T를 잡고 있다
        self.T.prev = self.H # 이렇게 되면 서로 붙잡고 있는 이중 연결 리스트가 완성됨

        self.size = 0 # 노드의 갯수 - 학생의 수라고 생각

    def isEmpty(self): #지금 기차놀이 중인 어린이가 한 명이라도 있는지 확인한다

        return self.size == 0  #이것도 위와 마찬가지로 학생의 수가 0명일 때 둘 중 아무거나 써도 상관없음


    def getNode(self, pos):
        p = self.H

        for i in range(0, pos):
            p = p.next
        return p #

    def insertFirst(self, data):
        p = self.H.next # 첫번재 어린이를 가리키거나, 비어잇다면 T를 가리키고 있겠지?

        node = Node(data,self.H, p)  # p의 이전 즉, 앞으로는 H를 잡고 있을 거고, 뒤로는 p 즉 T를 잡고 있는 모양이다
        self.H.next = node  # H가 T를 잡고 있다가 node로 바뀌게됨
        p.prev = node  # ?  여기 이해...

        self.size += 1

    def insertLast(self, data): # 가장 마지막에 넣는 거 이해.... 놓침
        p = self.T.prev

        node = Node(data, p, self.T)
        p.next = node
        self.T.prev = node

        self.size += 1


    def insert(self,data, pos):
        if pos < 1 or pos > self.size + 1:
            print('유효하지 않는 손잡기')
            return None

        p = self.getNode(pos) #항상 p를 기준으로 위치를 생각해라
        node = Node(data, p.prev, p) # p의 이전 즉, 앞으로는 H를 잡고 있을 거고, 뒤로는 p 즉 T를 잡고 있는 모양이다
        p.prev.next = node  #H가 T를 잡고 있다가 node로 바뀌게됨
        p.prev = node  # ?  여기 이해...

        self.size += 1

    def delete(self, pos):
        if self.isEmpty():
            print('emplty')
            return None

        if pos <1 or pos>self.size:
            print('유효하지 않음')
            return None
        p = self.getNode(pos)
        data = p.data

        p.prev.next = p.next
        p.next.prev = p.prev

        self.size -= 1
        return data

    def display(self): #
        p = self.H.next #

        while p!= self.T: # Tale 이 아니야?
            print(f"[{p.data}]--> ", end=" ") #
            if p.next != self.T: #
                print('<-->', end=" ") #
            p = p.next
        print()

if __name__ == '__main__':
    DL = DListType()

    DL.insert('a', 1)
    DL.insert('b', 1)
    DL.insert('c', 3)
    DL.insert('d', 2); DL.display(); input()

    print('DEl [%s] : ' % DL.delete(1), end='')
