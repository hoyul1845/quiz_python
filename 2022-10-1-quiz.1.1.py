# 2.1.1 연습 문제: 입력받은 숫자만큼 반복하기(while)

# 문제

# input()으로 사용자로부터 정수를 한 개 입력받아, 그 숫자를 숫자 크기만큼 반복해서 출력하는 파이썬 스크립트를 작성하세요. 이때 출력 앞에 공백을 한 칸 주어서, 입력과 출력이 구분되게 합니다.
# 단, while 문을 사용하세요.

# 예 1

# 입력:

# 3
# 출력:

#  3
#  3
#  3

# 예 2

# 입력:

# 5
# 출력:

#  5
#  5
#  5
#  5
#  5

#==================================================================

j = 0
i = int(input("입력:")) 
while j < i:
    print(i)
    j += 1