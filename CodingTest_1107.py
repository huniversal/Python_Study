# 피자 나눠먹기 - 3
# https://school.programmers.co.kr/learn/courses/30/lessons/120816
import math
def solution(slice, n):
    return math.ceil(n/slice)
#------------------------------------------------------------
# 순서쌍의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120836
def solution(n):
    answer = 0
    for i in range(1,n+1):
      if n % i == 0:
        answer += 1
    return answer
#------------------------------------------------------------