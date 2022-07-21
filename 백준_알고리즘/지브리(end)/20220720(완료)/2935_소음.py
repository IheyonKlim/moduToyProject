import math

# 10 제곱 확인 함수
def checkPowerOf10(number):
    intValue = math.log10(number)
    return intValue == math.floor(intValue)


# 1차 입력값 처리
def chkInput(inputFirst, userOpr, inputSecond):
    # 범위 체크 (10 ~ 1000000)
    if not (10 <= inputFirst, inputSecond <= 1000000):
        raise Exception('숫자의 범위가 잘못됐습니다.')

    # 10의 제곱 체크
    if not (checkPowerOf10(inputFirst) and checkPowerOf10(inputSecond)):
        raise Exception('10의 제곱이 아닙니다.')

    # 연산자 체크
    if not (userOpr == "+" or userOpr == "*"):
        raise Exception('숫자의 범위가 잘못됐습니다.')


# 결과값 계산
def calOutput(inputFirst, userOpr, inputSecond):
    resultValue = 0

    if userOpr == "+":
        resultValue = int(inputFirst) + int(inputSecond)
    elif userOpr == "*":
        resultValue = int(inputFirst) * int(inputSecond)

    return resultValue


try:
    inputFirst = int(input())
    userOpr = input()
    inputSecond = int(input())

    chkInput(inputFirst, userOpr, inputSecond)

    print(calOutput(inputFirst, userOpr, inputSecond))

except Exception as e:
    print(e)
