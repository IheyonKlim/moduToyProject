from collections import Counter

# 1차 입력값 처리
def chkInput(testCase=None):
    # 케이스 반복 횟수 체크
    caseLength = len(testCase)

    # 입력값이 3개가 아닐 때
    if caseLength != 3:
        raise Exception('입력값이 3개가 아닙니다.')
    for index in range(0, caseLength):
        # 주사위 값이 잘못 되었을 때
        if not (1 <= testCase[index] <= 6):
            raise Exception('입력값의 범위가 잘못되었습니다.')


# 결과값 계산
def calOutput(testCase=None):
    funcResult = 0

    numberA = testCase[0] # 1번째 수
    numberB = testCase[1] # 2번째 수

    dupList = dict(Counter(testCase)) # 중복 수 확인
    # ex 3 3 6
    # 딕셔너리 {3: 2, 6: 1}

    # 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
    if dupList.get(numberA) == 3:
        funcResult = 10000 + (numberA*1000)
    # 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
    elif dupList.get(numberA) == 2:
        funcResult = 1000 + (numberA*100)
    elif dupList.get(numberB) == 2:
        funcResult = 1000 + (numberB*100)
    # 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
    elif dupList.get(numberA) == 1:
        funcResult = max(testCase)*100

    return funcResult


try:
    caseInputList = list(map(int, input().split()))
    chkInput(caseInputList)
    print(calOutput(caseInputList))

except Exception as e:
    print(e)
