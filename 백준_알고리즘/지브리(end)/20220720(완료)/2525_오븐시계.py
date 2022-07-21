def chkInput(time, isCurTime):
    if isCurTime:
        userHour = time[0]
        userMin = time[1]

        if not (0 <= userHour <= 23) or not (0 <= userMin <= 59):
            raise Exception()
        return
    else:
        if not (0 <= time <= 1000):
            raise Exception()
        return


def calOutput(curTime, cookTime):
    hour = curTime[0]
    minute = curTime[1] + cookTime

    if minute >= 60:
        hour = (hour + int(minute / 60))
        minute = minute % 60
    if hour >= 24:
        hour = hour % 24

    func_result = [hour, minute]
    return func_result


try:
    userInput = list(map(int, input().split()))
    chkInput(userInput, True)
    userInput2 = int(input())
    chkInput(userInput2, False)

    result = calOutput(userInput, userInput2)
    print(result[0], result[1])
except:
    print('에러가 발생했습니다. 종료합니다.')
