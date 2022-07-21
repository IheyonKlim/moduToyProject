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

        # 케이스 반복 횟수 (0 ~ 8)
        if not (1 <= int(testCase[0]) <= 8):
            raise Exception('케이스 반복횟수가 잘못됐습니다.')


# 결과값 계산
def calOutput(testCaseList=None):
    funcResult = []

    for testCase in testCaseList:
        resultList = []
        resultSplit = list(testCase[1])

        for index in range(0, len(resultSplit)):
            caseRepCnt = int(testCase[0])
            while caseRepCnt > 0:
                caseRepCnt -= 1
                resultList.append(resultSplit[index])

        funcResult.append(resultList)

    return funcResult


try:
    caseCntInput = int(input())
    caseList = []
    resultList = []
    for index in range(0, caseCntInput):
        caseList.append(list(input().split()))

    chkInput(caseCntInput, caseList)
    resultList = calOutput(caseList)

    for result in resultList:
        print("".join(result))

except Exception as e:
    print(e)
