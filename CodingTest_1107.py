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
# 삼각형 완성 조건
# https://school.programmers.co.kr/learn/courses/30/lessons/120889
def solution(sides):
    answer = []
    answer.extend(sides)
    answer.sort(reverse = True)
    if answer[0] < answer[1] + answer[2]:
        return 1
    else:
        return 2
#------------------------------------------------------------
# 배열의 유사도 
# https://school.programmers.co.kr/learn/courses/30/lessons/120903
def solution(s1, s2):
    count = 0
    for item in s1:
        if item in s2:
            count += 1
    return count
#------------------------------------------------------------
# 자릿수 더하기 
# https://school.programmers.co.kr/learn/courses/30/lessons/120906
def solution(n):
    change = str(n)
    list_a = [int(i) for i in change]
    change_sum = sum(list_a)
    return change_sum