from arrayList import ArrayList

L = ArrayList(100)

while True:
    cmd = input("[메뉴]: i-입력, d-삭제, r- 변경, p-출력, l -읽기, s-저장, q- 종료 : ")

    if cmd == "i":
        pos = int(input('입력행 번호 : '))
        str = input('입력해 내용 : ')
        L.insert(pos,str)

    elif cmd == "d":
        pos = int(input('삭제행 번호 : '))
        L.delete(pos)

    elif cmd == "r":
        pos = int(input('변경행 번호 : '))
        str = input('변경해 내용 : ')
        L.replace(pos, str)

    elif cmd == "p":
        print('LIne Editor ')

        for line in range(L.size):
            print('[%d]' %line, end=' ')
            print(L.getEntry(line))

        print()

    elif cmd == "q":
        exit()
