class Node: # 어린이를 표현하기 위한 클래스
    def __init__(self, data, next = None): #어린이가 나가기위해선 data라는 이름표, next라는 허리끈
        self.data = data # data는 이름표
        self.next = next # next는 끈

class ListType: # 어린이집 반 = 햇님반, 달님반 등등
    def __init__(self):
        self.head = None #선생님을 설정 즉, self.head가 선생님을 나타낸 것
        self.size = 0 # 노드의 갯수 - 학생의 수라고 생각

    def isEmpty(self):
        return self.head is None # 선생님이 아무하고도 손을 잡지 않을 때
        #return self.size == 0  이것도 위와 마찬가지로 학생의 수가 0명일 때 둘 중 아무거나 써도 상관없음

    def getBefore(self, pos):
        p = self.head

        for i in range(1, pos -1):
            p = p.next

        return p # 주소를 return

    def insertFirst(self,data): # 누가 뭘잡고 뭘잡고?             단순연결에서 stack의 push와 유사하네 !!
        node = Node(data, self.head) #node가 보호자? Node(data) 는 어린이
        #보호자 손바닥에 어린이가 어디잇는지 적혀있어
        self.head = node # 선생님과 첫번째 어린이가 연결됨
        self.size += 1 # 학생수가 하나 추가 됨

    def insert(self,pos,data): # 어린이 한명이 들어와서 원하는 자리에 선택해서 손 잡을 수 있도록
        if pos < 1 or pos > self.size + 1: #지금 학생 3명 있는데 1,2,3번 하고 4번 자리까지 손 잡을 수 있음
            print('유효하지 않는 손잡기')
            return

        if pos == 1:
            self.insertFirst(data)
        else: # 여기가 핵심!!!!!!!!!!!!!!!!!(송교수님 왈)
            p = self.getBefore(pos )# p는 화살표 역할을 하는 변수
            node = Node(data, p.next)
            p.next = node  # 이제 누가 날 가리키지?
            self.size += 1


    def deleteFirst(self): # 연결된 리스트는 isfull체크 필요가 없음 대신에 empty 체크는 해야지!  -) 이건 사실상 스택의 pop과 같은 것이다
        if self.isEmpty(): # 비어있다면
            print('연결리스트가 비어있어서 delete 할 수 없음')
        else: #비어있지 않다면 첫번째 어린이가 삭제 되어야 하겠지?
            p = self.head
            self.head = p.next  #선생님은 이제 첫사람 대신 두번쨰 사람을 잡고 있어야겠지
            self.size -= 1  # 학생 한 명이 나가갔으니까 학생 수 -1 해줘야지
            return p.data

    def delete(self,pos): # 학생 삭제 ? deleteFirst와의 차이점은 뭘까
        if self.isEmpty():
            print('empty')
            return

        if pos == 1:
            return self.deleteFirst()
        else: #1번이 아닌  포지션을 삭제한다면 앞자리를 알아야함
            p = self.getBefore(pos)  # 삭제할 때는 이전 노드 뿐만이 아니라 삭제하는 노드의 포지션도 알아야함
            q = p.next # 삭제될 노드를 q로 지정

            p.next = q.next # q의 손위치
            self.size -= 1

            return q.data



    def display(self):
        p = self.head #p는 포인터처럼 화살표?

        while p: #p가 노드인 동안
            print(f"[{p.data}]--> ", end=" ") #화살표를 한 줄로 출력
            if p.next: # 다음 어린이가 있으면
                print('->', end=" ") #오로지 보기 좋게 표현한 것일 뿐
            p = p.next
        print()

# 이 위에 코드를 다 이해한다면 연결 리스트는 끝이다!! 이게 이해 되면 나머지도 다 할 수 있다
# 어려울 수 있지만 모르면 안되는 내용이다 ..... 단순 코드만 공부하는 게 아니라 순서도를 그리면서 차례에 맞게 풀어나가는 게 중요하단다..

if __name__ == "__main__": #테스트 코드
    L = ListType() # 햇님반 L을 만들었다 & 선생님이 한 명 생겼다 L.head가 하나 생겼다

    L.insertFirst('A'); L.insertFirst('B'); L.insertFirst('C'); L.display();input() #선생님 그리고 학생 A,B가 잘연결되었나 확인해야지

    L.insert(2, 'D'); L.display();
    L.insert(5, 'E'); L.display(); input(0)
    L.display()

'''
    print('%Del [%s] : ' % L.deleteFirst(), end=' ' )
    L.display()
'''
