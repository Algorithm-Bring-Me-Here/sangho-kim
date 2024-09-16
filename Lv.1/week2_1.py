# Lv.1 과일 장수
# https://school.programmers.co.kr/learn/courses/30/lessons/135808

# 사과 : 1~k점 (3~9)
# 한 상자에 사과 m개 (3~10)
# 상자 가격 = 사과 제일 낮은 점수 p * m
# score list(7~1,000,000)에서 사과 m개 추출한 최대 이익?

def solution(k, m, score):
    # 상자 개수 n
    n = len(score) // m

    # score 정렬
    score.sort(reverse=True)

    # m-1 부터 m번째 점수 n개 추출 후 계산
    answer = 0
    for i in range(n):
        answer += score[m-1+i*m] * m
    return answer