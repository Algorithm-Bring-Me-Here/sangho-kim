# Lv.1 키패드 누르기
# https://school.programmers.co.kr/learn/courses/30/lessons/67256

# 왼손 * 오른손 #
# 147 -> 왼손
# 369 -> 오른손
# 2580 -> 가까운 손, 거리 같으면 주손

def solution(numbers, hand):
    # *을 10, 0을 11, #을 12로 고려
    for i in range(len(numbers)):
        if (numbers[i] == 0):
            numbers[i] = 11

    # 초기값 설정
    left = 10
    right = 12
    answer = ''

    # 상황 별 로직
    for num in numbers:
        if (num in [1,4,7]):
            answer += "L"
            left = num
        elif (num in [3,6,9]):
            answer += "R"
            right = num
        else:
            # 거리 = 차이를 3으로 나눈 몫 + 나머지
            left_gap = abs(left - num)
            left_count = left_gap//3 + left_gap%3
            right_gap = abs(right - num)
            right_count = right_gap//3 + right_gap%3
            if (left_count > right_count):
                answer += "R"
                right = num
            elif (left_count < right_count):
                answer += "L"
                left = num
            else :
                if (hand == "right"):
                    answer += "R"
                    right = num
                else:
                    answer += "L"
                    left = num
    return answer