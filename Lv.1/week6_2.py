# Lv.1 달리기 경주
# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):

    # 딕셔너리 생성 (해시 테이블 -> 검색 O(1))
    player_dict = {p: i for i, p in enumerate(players)}

    for call in callings:
        # 순위 찾아서 리스트 swap
        before = player_dict[call]
        players[before], players[before-1] = players[before-1], players[before]
        # 딕셔너리 업데이트
        player_dict[players[before]] += 1
        player_dict[players[before-1]] -= 1
    return players