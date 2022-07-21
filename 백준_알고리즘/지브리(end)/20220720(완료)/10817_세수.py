# 입력값 처리
def chkInput(userInput):
    # 케이스 반복 횟수 체크
    for testCase in userInput:
        caseLength = len(userInput)

        # 입력값이 3개가 아닐 때
        if caseLength != 3:
            raise Exception('입력값이 3개가 아닙니다.')
        if not (1 <= int(testCase) <= 100):
            raise Exception('범위가 잘못 됐습니다.')


# 결과값 계산
def calOutput(inputFirst):
    return sorted(inputFirst)[1]

try:
    userInput = list(map(int, input().split()))
    chkInput(userInput)

    print(calOutput(userInput))

except Exception as e:
    print(e)
