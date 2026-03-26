from arrayStack import ArrayStack

S = ArrayStack()

msg= input("문자열 입력 받을래요? : ")
for c in msg:
    S.push(c)

print("문자열 출력 : ", end="")
while not S.isEmpty():
    print(S.pop(), end="") # 가장 늦게 입력받은 것부터 빼니까 거꾸로 출력되는 모습
print()
