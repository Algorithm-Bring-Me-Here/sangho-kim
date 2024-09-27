# Lv.2 이진 변환 반복하기
# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer = [0, 0]

    # 1까지 반복 진행
    while s != '1':
        answer[0] += 1
        answer[1] += s.count('0')
        # bin : 0b가 앞에 붙은채로 이진수 반환
        s = bin(len(s.replace('0', '')))[2:]
    return answer
