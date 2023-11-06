# 배열 원소의 길이 
# https://school.programmers.co.kr/learn/courses/30/lessons/120854
def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer
#------------------------------------------------------------
# 문자열 뒤집기 
# https://school.programmers.co.kr/learn/courses/30/lessons/120822
def solution(my_string):
    answer = ''
    for i in my_string:
        answer = my_string[::-1]
    return answer
#------------------------------------------------------------
# 특정 문자 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120826
def solution(my_string, letter):
    return my_string.replace(letter,'')
#------------------------------------------------------------
# 아이스아메리카노
# https://school.programmers.co.kr/learn/courses/30/lessons/120819
def solution(money):
    answer = [money//5500, money%5500]
    return answer