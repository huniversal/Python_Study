# n의 배수 고르기
# def solution(n, numlist):
#     answer = []
#     for i in numlist:
#         if i % n == 0:
#             answer.append(i)
#     return answer
#------------------------------------------------------------
# 대문자와 소문자 
def solution(my_string):
    answer = ''
    for i in my_string:
        check = i.isupper()
        if check == True:
            answer += i.lower()
        else:
            answer += i.upper()
    return answer
#------------------------------------------------------------