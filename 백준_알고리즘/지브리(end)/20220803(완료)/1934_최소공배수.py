# 1차 입력값 처리
def chkInput(caseCntInput, testCaseList=None):
    # 케이스 개수 체크 (1 ~ 1000)
    if not (1 <= caseCntInput <= 1000):
        raise Exception('케이스 갯수가 잘못됐습니다.')

    # 케이스 반복 횟수 체크
    for testCase in testCaseList:
        caseLength = len(testCase)

        # 입력값이 두개가 아닐 때
        if caseLength != 2:
            raise Exception('입력값이 2개가 아닙니다.')

        if not (1 <= testCase[0] <= 45000) or not (1 <= testCase[1] <= 45000):
            raise Exception('입력값의 범위가 잘못되었습니다.')


# 결과값 계산
def calOutput(testCaseList=None):
    funcResultList = []

    for testCase in testCaseList:
        numberA = int(testCase[0]) # 1번째 수
        numberB = int(testCase[1]) # 2번째 수

        # 2부터 순차적으로 곱해 서로 나눠지는 최소 값을 구함
        for mulIndex in range(1, (numberA * numberB)+1):
            if (numberA * mulIndex) % numberB == 0:
                funcResultList.append(numberA * mulIndex)
                break

    return funcResultList


try:
    caseCntInput = int(input())
    caseList = []
    for index in range(0, caseCntInput):
        caseList.append(list(map(int, input().split())))

    chkInput(caseCntInput, caseList)

    resultList = calOutput(caseList)
    for index in resultList:
        print(index)

except Exception as e:
    print(e)
