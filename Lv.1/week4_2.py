# Lv.1 [PCCP 기출문제] 1번 / 동영상 재생기
# https://school.programmers.co.kr/learn/courses/30/lessons/340213

def solution(video_len, pos, op_start, op_end, commands):
    for command in commands:
        mm = int(pos[:2])
        ss = int(pos[3:])

        op_st_mm = int(op_start[:2])
        op_st_ss = int(op_start[3:])
        op_end_mm = int(op_end[:2])
        op_end_ss = int(op_end[3:])

        # 오프닝 여부 확인 (시작부터 소요시간 비교)
        if (op_st_mm <= mm and mm <= op_end_mm):
            op_time = op_end_ss - op_st_ss + (op_end_mm - op_st_mm)*60
            pos_time = ss - op_st_ss + (mm - op_st_mm)*60
            if (op_time > pos_time and pos_time >= 0):
                pos = op_end

        mm = int(pos[:2])
        ss = int(pos[3:])

        # 뒤로가기
        if (command == "prev"):
            ss -= 10
            if (ss < 0):
                ss += 60
                mm -= 1
            if (mm < 0):
                pos = "00:00"
            else:
                pos = str(mm).zfill(2) + ":" + str(ss).zfill(2)

        # 앞으로 가기
        else:
            ss += 10
            if (ss >= 60):
                ss -= 60
                mm += 1
            video_time = int(video_len[:2])*60 + int(video_len[3:])
            pos_time = mm*60 + ss
            if (video_time < pos_time):
                pos = video_len
            else:
                pos = str(mm).zfill(2) + ":" + str(ss).zfill(2)

        mm = int(pos[:2])
        ss = int(pos[3:])

        # 오프닝 여부 다시 확인 (시작부터 소요시간 비교)
        if (op_st_mm <= mm and mm <= op_end_mm):
            op_time = op_end_ss - op_st_ss + (op_end_mm - op_st_mm)*60
            pos_time = ss - op_st_ss + (mm - op_st_mm)*60
            if (op_time > pos_time and pos_time >= 0):
                pos = op_end

    return pos