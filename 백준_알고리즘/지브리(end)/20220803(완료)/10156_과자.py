from collections import Counter

# 1차 입력값 처리
def chkInput(testCase=None):
    # 케이스 반복 횟수 체크
    caseLength = len(testCase)

    # 입력값이 3개가 아닐 때
    if caseLength != 3:
        raise Exception('입력값이 3개가 아닙니다.')

    # 과자 한개 가격 범위 체크
    if not (1 <= testCase[0] <= 1000):
        raise Exception('입력값의 범위가 잘못되었습니다.')

    # 사려고 하는 과자 개수 범위 체크
    if not (1 <= testCase[1] <= 1000):
        raise Exception('입력값의 범위가 잘못되었습니다.')

    # 현재 동수가 가진 돈 범위 체크
    if not (1 <= testCase[2] <= 100000):
        raise Exception('입력값의 범위가 잘못되었습니다.')


# 결과값 계산
def calOutput(testCase=None):
    funcResult = 0

    snackPrice = testCase[0] # 과자 한개 가격
    wtbSnackCnt = testCase[1] # 사려고 하는 과자 개수
    money = testCase[2] # 현재 동수가 가진 돈

    # 가진 돈이 적을 때
    if snackPrice * wtbSnackCnt > money:
        # 절대값
        funcResult = abs(money - snackPrice * wtbSnackCnt)
    else:
        # 가진 돈이 같거나 많을 때
        funcResult = 0

    return funcResult


try:
    caseInputList = list(map(int, input().split()))
    chkInput(caseInputList)
    print(calOutput(caseInputList))

except Exception as e:
    print(e)
