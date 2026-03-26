from scipy.special.cython_special import eval_sh_legendre

from arrayStack import ArrayStack

def checkBrackets(str):
    S = ArrayStack()

    pairs = {

        ']' : '[',
        '}' : '{',
        ')' : '('

    }    #pairs['}'] -> '{'   & 딕셔너리는 key 와 value 로 이루어져있다.. key:value
    for c in str:
        if c in '[{(':
            S.push(c)
        elif c in ']})':
            if S.isEmpty():
                return "조건 2에 대하여 위배한 것이다."
            else:
                if S.pop() != pairs[c]: # 조건 3에 대하여 위배한 경우이다.
                    return "조건 3에 대하여 위배한 것이다."

    if not S.isEmpty():
        return "조건 1에 대하여 위배한 것이다"

    else:
        return "매칭이 성공했습니다."


if __name__ == "__main__":
    str = input("수식입력하세요: ")

    print(str,'----->',checkBrackets(str))
