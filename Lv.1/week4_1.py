# Lv.1 기사단원의 무기
# https://school.programmers.co.kr/learn/courses/30/lessons/136798?language=python3

def solution(number, limit, power):
    answer = 0

    for i in range(number+1):
        # 약수 개수 세기 (루트n까지)
        count = 0
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                count += 1
                # 루트n이 정수인 경우 고려
                if (j ** 2) != i:
                    count += 1

        # 공격력 비교
        if count > limit:
            answer += power
        else:
            answer += count

    return answer