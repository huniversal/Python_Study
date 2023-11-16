# 백준 문제
# https://www.acmicpc.net/problem/1546
def solution(n, score):
    max_score = int(max(score))
    new_score = []
    for i in score:
        new_score.append(i / max_score * 100)
    new_average = sum(new_score) / n
    return new_average

print(solution(3, [40, 80, 60]))
#------------------------------------------------------------