from arrayStack import ArrayStack

def evalPostfix(expr):  # 후위 표기식을 계산하는 함수
    S = ArrayStack()

    for token in expr:
        if token in '+-*/':
            val2 = S.pop()
            val1 = S.pop()

            if token == '+':
                S.push(val1 + val2)
            elif token == '-':
                S.push(val1 - val2)
            elif token == '*':
                S.push(val1 * val2)
            elif token == '/':
                S.push(val1 / val2)
        else:
            S.push(float(token)) # 형변환
    '''
    if S.top != 0:
        S.push(float(expr[S.top - 1]))
    '''
    return S.pop()

if __name__ == '__main__': #실행 함수
    str = '8 2 / 3 - 3 2 * +'
    expr = str.split()

    print(expr, '---->', evalPostfix(expr))
