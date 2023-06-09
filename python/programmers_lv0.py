# 문자열 출력하기
str = input()
print(str)

# a와 b 출력하기
a, b = map(int, input().strip().split(' '))
print('a =', a)
print('b =', b)

# 문자열 반복해서 출력하기
a, b = input().strip().split(' ')
b = int(b)
print(a * b)

# 대소문자 바꿔서 출력하기
str = input()
index = ""
for i in str:
    if i.islower():
        index += i.upper()
    else:
        index += i.lower()
print(index)

# 특수문자 출력하기
print('!@#$%^&*(\\\'"<>?:;')

# 덧셈식 출력하기
a, b = map(int, input().strip().split(' '))
print(f'{a} + {b} = {a + b}')

# 문자열 붙여서 출력하기
str1, str2 = input().strip().split(' ')
print(f'{str1}{str2}')
#print(str1 + str2)
#print(input().strip().replace(' ', ''))

# 문자열 돌리기
str = input()
for i in str:
    print(i)
	

# 홀짝 구분하기
a = int(input())
if a % 2 == 0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')

# 문자열 겹쳐쓰기
def solution(my_string, overwrite_string, s):
    os_len = len(overwrite_string) + s
    return my_string[:s] + overwrite_string + my_string[os_len:]
# -- 안되는 예제
def solution(my_string, overwrite_string, s):
    os_len = len(overwrite_string) + s
    return my_string.replace(my_string[s:os_len], overwrite_string)

# 문자열 섞기
def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i]
        answer += str2[i]
    return answer

# 문자 리스트를 문자열로 변환하기
def solution(arr):
    return ''.join(arr)

# 문자열 곱하기
def solution(my_string, k):
    answer = my_string * k
    return answer

# 더 크게 합치기
def solution(a, b):  
    if (str(a) + str(b)) > (str(b) + str(a)):
        answer = str(a) + str(b)
    elif (str(a) + str(b)) == (str(b) + str(a)):
        answer = str(a) + str(b)
    else:
        answer = str(b) + str(a)
    return int(answer)

def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))

# 두 수의 연산값 비교하기
def solution(a, b):
    return max(int(f"{a}{b}"), a*b*2)

# n의 배수
def solution(num, n):
    return 1 if num % n == 0 else 0
# 파이썬의 삼항연산자
# [참일때] if [조건문] else [거짓일때]


# 공배수
def solution(number, n, m):
    return 1 if number % n == 0 and number % m == 0 else 0

# 홀짝에 따라 다른 값 반환하기


# 조건 문자열


# flag에 따라 다른 값 반환하기
def solution(a, b, flag):
    return a + b if flag == True else a - b

# 코드 처리하기


# 등차수열의 특정한 항만 더하기


# 주사위 게임 2
def solution(a, b, c):
    cnt = 0
    if a != b != c and a != c:
        cnt = a + b + c
    elif a != b == c or a == b != c or a == c != b:
        cnt = (a + b + c) * ((a ** 2)+ (b ** 2) + (c ** 2))
    elif a == b == c:
        cnt = (a + b + c) * ((a ** 2)+ (b ** 2) + (c ** 2)) * ((a ** 3)+ (b ** 3) + (c ** 3))
    return cnt

# 원소들의 곱과 합
def solution(num_list):
    cnt = 1
    for i in num_list:
        cnt *= i 
    return 1 if (sum(num_list) ** 2) > cnt else 0


# 이어 붙인 수


# 마지막 두 원소


# 수 조작하기 1


# 수 조작하기 2


# 수열과 구간 쿼리 3


# 수열과 구간 쿼리 2



# 수열과 구간 쿼리 4



# 배열 만들기 2



# 카운트 업


# 콜라츠 수열 만들기



# 배열 만들기 4



# 간단한 논리 연산



# 주사위 게임 3



# 글자 이어 붙여 문자열 만들기



# 9로 나눈 나머지



# 문자열 여러 번 뒤집기







# 중복된 문자 제거
def solution(my_string):
    result = ''
    for i in my_string:
        if i not in result:
            result += i
    return result

# 모음 제거
def solution(my_string):
    string = 'aeiou'
    for i in string:
        my_string = my_string.replace(i,'')
    return my_string


# 특정 문자 제거하기
def solution(my_string, letter):
    for i in letter:
        my_string = my_string.replace(i,'')
    return my_string

# 숨어있는 숫자의 덧셈(1)
def solution(my_string):
    cnt = 0
    for i in my_string:
        if i.isdigit():
            cnt += int(i)
    return cnt

def solution(my_string):
    return sum([int(i) for i in my_string if i.isdigit()])

def solution(my_string):
    return sum(map(int, filter(lambda x:x.isdigit(), my_string)))

import re
def solution(my_string):
    return sum([int(i) for i in re.sub('[^1-9]', '', my_string)])

# 숨어있는 숫자의 덧셈(2)
import re

def solution(my_string):
    return sum(map(int, re.findall(r'[0-9]+', my_string)))


# 중복된 숫자 갯수
def solution(array, n):
    return array.count(n)

# 머쓱이보다 키 큰 사람
def solution(array, height):
    cnt = 0
    for i in array:
        if i > height:
            cnt += 1
    return cnt

# 옹알이(1)
import re

def solution(babbling):
    cnt = 0
    li = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in li:
            if j * 2 not in i:
                i = i.replace(j, ' ')
        if len(i.strip()) == 0:
            cnt += 1

    return cnt


