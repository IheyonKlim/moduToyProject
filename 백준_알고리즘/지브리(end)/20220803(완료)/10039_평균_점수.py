# 입력값 처리
def chkInput(userInput):
    for testCase in userInput:

        # 점수는 모두 0점 이상, 100점 이하인 5의 배수
        if not (0 <= testCase <= 100) and not (testCase % 5 == 0):
            raise Exception('범위가 잘못 됐습니다.')


# 결과값 계산
def calOutput(userInputList):
    resultValue = 0

    for testCase in userInputList:
        if testCase < 40:
            resultValue += 40
        else:
            resultValue += testCase

    return int(resultValue/len(userInputList))

try:
    userInputList = []
    userInputCnt = 5

    for index in range(0, userInputCnt):
        userInputList.append(int(input()))

    chkInput(userInputList)
    print(calOutput(userInputList))

except Exception as e:
    print(e)