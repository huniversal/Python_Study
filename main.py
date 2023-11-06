# def add(x, y):
#   return x+y

# lambda x, y: x+y 

# if 2==2:
#   print(True)
# else:
#   print(False)

# print( True if 2==2 else False )


def calc(x, y):
  return x+y, x-y, x*y, x/y

a, b, c, d = calc(10,2)

# P.318
*a, b = [10, 20, 30]
c, d = (10, 20)
print(a, b)
# -> 언패킹
print()

a = 10, 20, 30
b = (10, 20, 30)
print(a, b)
# -> 패킹

# 리스트 A가 주어지고 A리스트가 홀수이면서 3의 배수인것만 리스트로 다시 만들어라
# A의 범위 : 1~ 101
a = [ i for i in range(1, 101) if i/2!=0 and i/3==0 ]

