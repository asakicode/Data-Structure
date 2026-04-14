from arrayStack import ArrayStack

def precedence(op): #각 연산자마다의 우선 순위를 부여하는 함수
    if op in '+-':
        return 1
    elif op == '*/':
        return 2
    else: # 0점에 해당하는 건 괄호겠지?
        return 0


def infixToPostfix(expr):
    S = ArrayStack()

    for term in expr: #수식을 읽고 있어요
        if term == '(': # 괄호를 만나면 무조건 push 하게
            S.push(term)

        elif term == ')':
            while not S.isEmpty() and S.peak() != '(':
                print(S.pop(), end=' ')
            S.pop()

        elif term in '+-*/':
            while not S.isEmpty():
                op = S.peak()
                if(precedence(term) <= precedence(op)):
                    print(S.pop(), end=' ')
                else:
                    break
            S.push(term)
        else:
            print(term, end=' ')

    while not S.isEmpty():
        print(S.pop(), end=' ')

if __name__ == '__main__':
    infix = input('Enter your expression(중위식이나 입력하세요ㅋ 공백으로 구분해야함): ')
    expr = infix.split()
    infixToPostfix(expr)
