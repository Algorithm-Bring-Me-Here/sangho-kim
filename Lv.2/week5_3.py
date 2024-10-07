# Lv.2 2022 KAKAO BLIND RECRUITMENT - k진수에서 소수 개수 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def change_n_to_k(n,k):
    n_to_k = ""
    while n>0:
        n_to_k += str(n % k)
        n //= k
    return n_to_k[::-1]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    # k진수 변환
    n_to_k = change_n_to_k(n,k)

    # 0 기준으로 구별
    array = n_to_k.split("0")

    # 각 숫자 소수 판정
    count = 0
    for num in array:
        if num != "" and num != "1":
            if is_prime(int(num)):
                count += 1

    return count