# 입력 값 체크
def chkInput(userInput):
    if not 1 <= userInput <= 4294967295:
        raise Exception('범위가 잘못 됐습니다.')


# 결과값 계산
def calOutput(userInput):
    numSeq = 0
    result = 0
    for i in range(1, userInput + 1):
        result += i
        numSeq += 1
        if result > userInput:
            numSeq -= 1
            break
            
    return numSeq

try:
    userInput = int(input())
    chkInput(userInput)
    print(calOutput(userInput))

except Exception as e:
    print(e)
