# @ = x3
# % = +5
# # = -7
# 입력값
#   T = 테스트케이스 갯수
#   화성 수학식 한줄에 하나씩 (연산자 최대 3개)
#   값 (0~100), 소수점 한자리까지
# 출력
#   소수점 둘째 자리까지

# 1차 입력값 처리 : marsCase[0] (0~100)
def chkInput(testCaseList=None):
    marsOpr = ["@", "%", "#"]

    # 연산자 개수 및 값 체크( 최대 3개 )
    for marsCase in testCaseList:
        caseLength = len(marsCase)
        # 연산자 3개 이상일 경우 Exception
        if caseLength > 4:
            raise Exception()
        # 화성 연산자가 없을 경우 Exception
        for index in range(1, caseLength):
            if marsCase[index] not in marsOpr:
                raise Exception()
        # marsCase[0] 0 ~ 100 아닐 경우 Exception
        if not (0 <= float(marsCase[0]) <= 100):
            raise Exception()


# 결과값 계산
def calOutput(testCaseList=None):
    funcResult = []
    for marsCase in testCaseList:
        caseTmp = float(marsCase[0])
        # @ = x3    % = +5    # = -7
        for index in range(1, len(marsCase)):
            if "@" == marsCase[index]:
                caseTmp *= 3
            elif "%" == marsCase[index]:
                caseTmp += 5
            elif "#" == marsCase[index]:
                caseTmp -= 7

        funcResult.append(format(caseTmp, ".2f"))

    return funcResult


try:
    caseCntInput = int(input())
    caseList = []
    result = []
    for index in range(0, caseCntInput):
        caseList.append(list(input().split()))

    chkInput(caseList)
    result = calOutput(caseList)

    for index in range(0, len(result)):
        print(result[index])

except Exception as e: print(e)
