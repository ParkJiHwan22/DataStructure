## 함수 선언 부분 ##
def printPoly(t_x , p_x):
    polyStr = "P(x) = "

    for i in range(len(px)):
        term = t_x[i]       # 항 차수
        coef = p_x[i]       # 계수

        if (coef >= 0):
            polyStr += "+"
        polyStr += str(coef) + "X^" + str(term) + " "

    return polyStr


def calcPoly(xVal, t_x, p_x):
    retValue = 0
    term = len(p_x) - 1     # 최고차항 숫자 = 배열 길이 - 1

    for i in range(len(px)):
        term = t_x[i]   # 항 차수
        coef = p_x[i]   # 계수
        retValue += coef * xVal ** term

    return retValue


## 전역 변수 선언 부분 ##
tx = [300, 20, 0]
px = [7, -4, 5]      # 7x^3 - 4x^2 + 0x^1 + 5x^0


## 메인 코드 부분 ##
if __name__ == "__main__":

    pStr = printPoly(tx, px)
    print(pStr)

    xValue = int(input("X 값-->"))

    pxValue = calcPoly(xValue, tx, px)
    print(pxValue) 