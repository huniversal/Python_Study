# 가위 바위 보
def solution(rsp):
    win_rsp = {"2" : "0", "0" : "5", "5" : "2"}
    answer = []
    for i in list(rsp):
        answer.append(win_rsp[i])
    return "".join(answer)
#------------------------------------------------------------