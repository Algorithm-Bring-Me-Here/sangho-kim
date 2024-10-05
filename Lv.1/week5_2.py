# Lv.1 바탕화면 정리
# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    isInitial = True
    for x in range(len(wallpaper)):
        for y in range(len(wallpaper[x])):
            if wallpaper[x][y] == "#":
                # 초기값 설정
                if isInitial:
                    lux, luy, rdx, rdy = x,y,x+1,y+1
                    isInitial = False
                # 최대 최소 비교
                lux = min(lux, x)
                luy = min(luy, y)
                rdx = max(rdx, x+1)
                rdy = max(rdy, y+1)

    answer = [lux, luy, rdx, rdy]
    return answer

# (추가 노트)
# 초기값 설정 없이 그냥 x축 y축 따로 리스트 받고 마지막에 max, min 비교도 가능
def solution(wall):
    a, b = [], []
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]