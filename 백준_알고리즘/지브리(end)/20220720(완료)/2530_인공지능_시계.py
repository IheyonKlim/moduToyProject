# 1차 입력값 처리 : userHour 시간(0 ~ 23), userMin 분(0 ~ 59), userSec 초(0 ~ 59)
def chkInput(time, isCurTime):
    # 1차 입력값 체크
    if isCurTime:
        # 입력 값 개수 체크
        if len(time) != 3:
            raise Exception()

        userHour = time[0]
        userMin = time[1]
        userSec = time[2]

        # 값 체크
        if not (0 <= userHour <= 23) or not (0 <= userMin <= 59):
            raise Exception()
        elif not (0 <= userMin <= 59):
            raise Exception()
        elif not (0 <= userSec <= 59):
            raise Exception()

    # 2차 입력값 체크
    else:
        if not (0 <= time <= 500000):
            raise Exception()


# 2차 입력값 처리 : curTime 초 (0 ~ 500000)
def calOutput(curTime, cookTime):
    hour = curTime[0]
    minute = curTime[1]
    second = curTime[2] + cookTime

    if second >= 60:
        minute = (minute + int(second / 60))
        second %= 60
    if minute >= 60:
        hour = (hour + int(minute / 60))
        minute %= 60
    if hour >= 24:
        hour %= 24

    func_result = [hour, minute, second]
    return func_result


try:
    userInput = list(map(int, input().split()))
    chkInput(userInput, True)
    userInput2 = int(input())
    chkInput(userInput2, False)

    result = calOutput(userInput, userInput2)
    #print(userInput[0], userInput[1], userInput[2])
    #print(userInput2)
    print(result[0], result[1], result[2])
except:
    print('에러가 발생했습니다. 종료합니다.')
