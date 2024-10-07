# Lv.1 2016년
# https://school.programmers.co.kr/learn/courses/30/lessons/12901?language=python3

def solution(a, b):
    # 요일, 초기 날짜 설정
    day_dict = {0:"SUN", 1:"MON", 2:"TUE", 3:"WED", 4:"THU", 5:"FRI", 6:"SAT"}
    count_dict = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30}
    date = 4

    # 월,일 계산해서 추가
    for i in range(1,a):
        date += count_dict[i]
    date += b

    # 요일 계산
    day = day_dict[date % 7]
    return day


# (추가 노트)
# 두 리스트의 key값이 0,1,2 이어서, dict 대신 list로 가는게 더 좋을 듯