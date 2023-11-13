# 옷가게 할인 받기
# def solution(price):
#     if price >= 100000 and price < 300000:
#         return int(price * 0.95)
#     elif price >= 300000 and price < 500000:
#         return int(price * 0.9)
#     elif price >= 500000:
#         return int(price * 0.8)
#     else:
#         return int(price)
#------------------------------------------------------------
# 외계행성의 나이
# def solution(age):
#     answer = ''
#     for i in str(age):
#         answer += chr(int(i) + 97)
#     return answer
#------------------------------------------------------------
# 중복된 문자 제거 
# def solution(my_string):
#   answer = ''
#   for i in my_string:
#     if i not in  answer:
#       answer += i
#   return answer
#------------------------------------------------------------
# 제곱수 판별하기
# def solution(n):
#     for i in range(n):
#         if i**2 == n:
#             return 1
#     return 2
#------------------------------------------------------------
# 문자 반복 출력하기 
def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i*n
    return answer
#------------------------------------------------------------

