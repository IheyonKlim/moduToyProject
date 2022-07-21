# 1차 입력값 처리
def chkInput():
    chkZero = False
    userInputList = []
    listIndex = 0

    # 0, 0 이 나올 때 까지 사용자 입력값을 받음
    while not chkZero :
        userInputList.append(list(map(int, input().split())))
        if max(userInputList[listIndex]) == 0:
            chkZero = True
            continue
        else:
            listIndex += 1

    # 케이스 반복 횟수 체크
    for testCase in userInputList:
        caseLength = len(testCase)

        # 입력값이 두개가 아닐 때
        if caseLength != 2:
            raise Exception('입력값이 2개가 아닙니다.')

        if not (0 <= testCase[0] <= 1000000) or not (0 <= testCase[1] <= 1000000):
            raise Exception('입력값의 범위가 잘못되었습니다.')

    userInputList.pop() # 마지막 요소 제거
    return userInputList


# 결과값 계산
def calOutput(testCaseList=None):
    funcResultList = []

    for index in range(0, len(testCaseList)):
        if testCaseList[index][0] > testCaseList[index][1]:
            funcResultList.append("Yes")
        else:
            funcResultList.append("No")

    return funcResultList


try:
    userInputList = chkInput()
    resultList = calOutput(userInputList)
    for index in resultList:
        print(index)

except Exception as e:
    print(e)
