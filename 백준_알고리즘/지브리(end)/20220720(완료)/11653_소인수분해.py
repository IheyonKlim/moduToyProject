# 입력값 처리
def chkInput(userInput):
    # 입력값 체크
    if not (1 <= userInput <= 10000000):
        raise Exception('범위가 잘못 됐습니다.')


# 결과값 계산
def calOutput(inputFirst):
    # 나뉠 최대 값
    maxRange = inputFirst
    # 결과값 저장
    targetList = []
    #초기 값
    target = 2
    
    # 더이상 나눠지지 않을 때 까지
    while maxRange != 1:
        # 나머지 0 일경우에만 나눔
        if maxRange % target == 0:
            # 최대값이 나눈수로 바뀐다.
            maxRange = maxRange / target
            targetList.append(target)
            # 다시 처음부터 시작
            target = 2
        else:
            target += 1
    return targetList

try:
    userInput = int(input())
    chkInput(userInput)
    targetList = calOutput(userInput)
    for printTarget in targetList:
        print(printTarget)

except Exception as e:
    print(e)
