# 백준 문제
# https://www.acmicpc.net/problem/1546
# def solution(n, score):
#     max_score = int(max(score))
#     new_score = []
#     for i in score:
#         new_score.append(i / max_score * 100)
#     new_average = sum(new_score) / n
#     return new_average

# print(solution(3, [40, 80, 60]))
#------------------------------------------------------------
# 개미 군단
# def solution(hp):
#   power_list = [5, 3, 1]
#   ant_count = [0,0,0]
#   for i in range(len(power_list)):
#     ant_count[i] = hp // power_list[i]
#     hp %= power_list[i]
#   total = sum(ant_count)
#   return total
#------------------------------------------------------------
# 백준 문제 
# https://www.acmicpc.net/problem/2839 
def solution(n): 
  count = 0 
  while n >= 0: 
    if n % 5 == 0: 
      count += (n // 5)  
      return count 
    n -= 3 
    count += 1 
  else: 
    return (-1) 
print(solution(4)) 
#------------------------------------------------------------ 


