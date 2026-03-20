class ArrayList:
    def __init__(self, capacity):
        self.capacity = capacity  # [수정] 오타 교정: capactiy -> capacity
        self.array = [None] * self.capacity
        self.size = 0  # [수정] 초기값 0으로 설정 필수

    def isEmpty(self):
        return self.size == 0  # [수정] self.size로 참조

    def isFull(self):
        return self.size == self.capacity  # [수정] self.capacity로 참조

    def insert(self, pos, e):
        # [수정] if문 문법 교정 (콜론 위치 및 self 참조)
        if not self.isFull() and 0 <= pos <= self.size:
            # [수정] 들여쓰기 교정: for문부터 self.size까지 if문 안으로 포함
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i - 1]

            self.array[pos] = e
            self.size += 1
        else:
            # [수정] 불필요한 def insert 중복 선언 제거
            print("overflow or invalid position")

    def delete(self, pos):
        # [수정] global size 삭제: 클래스 내부 변수는 self.size를 사용함
        # [수정] 삭제 조건: pos는 size보다 작아야 함 (pos < self.size)
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]

            # [수정] 연필이 필요한 범위 설정!
            # 삭제 위치(pos)부터 마지막 데이터 바로 전(size-1)까지 돌며
            # 다음 칸(i+1)의 데이터를 현재 칸(i)으로 땡겨옵니다.
            for i in range(pos, self.size - 1):
                self.array[i] = self.array[i + 1]

            self.size -= 1
            return e
        else:
            print('underflow or invalid position')


    def replace(self,pos,e):
        if 0 <= pos < self.size:
            self.array[pos] = e
        else:
            pass



    def getEntry(self,pos):
        if 0<= pos<self.size:
            return self.array[pos]
        else:
            None

    def __str__(self):
        return str(self.array[0:self.size])


# 테스트 코드
if __name__ == '__main__':
    L1 = ArrayList(20)
    L1.insert(0, 10)
    L1.insert(1, 20)
    L1.insert(2, 30)
    L1.insert(3, 40)
    # L1.insert(5, 50) -> 4번 인덱스가 비어있으므로 유효하지 않은 위치로 출력됨
    L1.insert(4, 50)

    print(f"현재 리스트: {L1}")
    print(f"삭제된 값: {L1.delete(1)}")  # 20 삭제
    print(f"삭제 후 리스트: {L1}")
