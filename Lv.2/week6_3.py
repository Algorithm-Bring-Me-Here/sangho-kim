# Lv.2 카펫
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    # 노란색 세로 위해 약수 출력 (제곱)
    for col in range(1, int(yellow**0.5)+1):
        if yellow % col == 0:
            row = yellow / col
            # 갈색 개수 비교
            if (4 + row*2 + col*2) == brown:
                return [row+2, col+2]