# 평균값 = 멜로디 개수 / 곡 개수 (올림)
# 입력값 곡 개수(1~), 평균값(~100)
# 멜로디 개수 = 평균값 * 곡 개수
import math


# 1차 입력값 처리 : 입력값 곡 개수(1~), 평균값(~100)
def chkInput(chkUserInput):
    # 입력 값 개수 체크
    if len(chkUserInput) != 2:
        raise Exception()

    userSongs = chkUserInput[0]
    userAvgMel = chkUserInput[1]

    # 값 체크
    if not (1 <= userSongs):
        raise Exception()
    elif not (0 <= userAvgMel <= 100):
        raise Exception()


# 결과값 출력
def calOutput(chkUserInput):
    userSongs = chkUserInput[0]
    userAvgMel = chkUserInput[1]

    # 멜로디 개수 = 평균값 * 곡 개수
    maxMelCount = userSongs * userAvgMel

    # 평균값 = 멜로디 개수 / 곡 개수 (올림)
    while maxMelCount >= 1:
        melody = maxMelCount / userSongs
        melody = math.ceil(melody)  # 값 올림
        if melody < userAvgMel:
            return maxMelCount + 1

        maxMelCount -= 1

    return 0


try:
    userInput = list(map(int, input().split()))
    chkInput(userInput)
    result = calOutput(userInput)
    #print(userInput[0], userInput[1])
    print(result)
except:
    print('에러가 발생했습니다. 종료합니다.')
