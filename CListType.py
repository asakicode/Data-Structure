class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class CircularListType:
    def __init__(self):
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def insertLast(self, data):
        node = Node(data)

        if self.isEmpty(): #비어있을떄 내가 처음 들어가면?
            self.tail = node
            node.next = self.tail  # 나는 나를 잡는 형태?
        else: #비어있지 않은 상태에서 새로운 놈이 마지막 노드로 들어간다면?
            node.next = self.tail.next # 나는 누굴 잡지 -> 나는 기존의 마지막 놈을 잡으면 됨
            self.tail.next = node #누가 날 잡지? -> 기존의 마지막이었던 놈이 날 잡고
            self.tail = node #누가 또 날 잡을지 -> 선생이 날 잡고
            

    def insertFirst(self, data):
        node = Node(data)

        if self.isEmpty(): #비어있을떄 내가 처음 들어가면?
            self.tail = node
            node.next = self.tail  # 나는 나를 잡는 형태?
            
        else: #비어있지 않은 상태에서 새로운 놈이 마지막 노드로 들어간다면?
            node.next = self.tail.next # 나는 누굴 잡지 -> 나는 기존의 마지막 놈을 잡으면 됨
            self.tail.next = node #누가 날 잡지? -> 기존의 마지막이었던 놈이 날 잡고
