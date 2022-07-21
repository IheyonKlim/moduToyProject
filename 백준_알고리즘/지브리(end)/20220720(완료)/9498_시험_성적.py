# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

# 입력값 처리
def chkInput(inputFirst):
    # 범위 체크 (0 ~ 100)
    if not (0 <= inputFirst <= 100):
        raise Exception('숫자의 범위가 잘못됐습니다.')


# 결과값 계산
def calOutput(inputFirst):
    resultValue = ""

    if inputFirst >= 90 :
        resultValue = "A"
    elif inputFirst >= 80 :
        resultValue = "B"
    elif inputFirst >= 70 :
        resultValue = "C"
    elif inputFirst >= 60 :
        resultValue = "D"
    else :
        resultValue = "F"

    return resultValue


try:
    inputFirst = int(input())
    chkInput(inputFirst)

    print(calOutput(inputFirst))

except Exception as e:
    print(e)