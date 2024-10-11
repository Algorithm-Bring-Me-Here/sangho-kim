# Lv.1 모의고사
# https://school.programmers.co.kr/learn/courses/30/lessons/42840

man1 = [1,2,3,4,5]
man2 = [2,1,2,3,2,4,2,5]
man3 = [3,3,1,1,2,2,4,4,5,5]
result = [[1,0], [2,0], [3,0]]

def solution(answers):
    for i in range(len(answers)):
        if answers[i] == man1[i%5]:
            result[0][1] += 1
        if answers[i] == man2[i%8]:
            result[1][1] += 1
        if answers[i] == man3[i%10]:
            result[2][1] += 1

    winner = []
    score = 0
    for j in range(3):
        if score < result[j][1]:
            winner = [j+1]
            score = result[j][1]
        elif score == result[j][1]:
            winner.append(j+1)

    return winner