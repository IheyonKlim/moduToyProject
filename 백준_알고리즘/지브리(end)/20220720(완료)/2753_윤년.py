# 1차 입력값 처리
def chkInput(caseCntInput):
    # 범위 체크 (1 ~ 4000)
    if not (1 <= caseCntInput <= 4000):
        raise Exception('값의 범위가 잘못됐습니다.')


# 결과값 계산
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
def calOutput(caseCntInput):
    result = 0  # 윤년이면 1, 아니면 0을 출력한다.

    if (caseCntInput % 4 == 0) and (not (caseCntInput % 100 == 0) or (caseCntInput % 400 == 0)):
        result = 1

    return result


try:
    caseCntInput = int(input())
    chkInput(caseCntInput)
    print(calOutput(caseCntInput))

except Exception as e:
    print(e)
