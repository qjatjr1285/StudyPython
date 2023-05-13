# Day 1 사칙연산
# 두 수의 합
def solution(num1, num2):
    return num1 + num2

# 두 수의 차
def solution(num1, num2):
    return num1 - num2

# 두 수의 곱
def solution(num1, num2):
    return num1 * num2

# 몫 구하기
def solution(num1, num2):
    return num1 // num2

# Day 2 사칙연산, 조건문, 배열
# 두 수의 나눗셈
def solution(num1, num2):
    return int((num1 / num2) * 1000)

# 숫자 비교하기
def solution(num1, num2):
    return 1 if num1 == num2 else -1

# 분수의 덧셈
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(numer1, denom1, numer2, denom2):
    bm = denom1 * denom2
    bj = (numer1 * denom2) + (numer2 * denom1)
    
    a = gcd(bm, bj)
    
    answer = [bj // a, bm // a]
    return answer

# 배열 두 배 만들기
def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i*2)
    return answer

# Day 3 사칙연산, 배열, 수학
# 나머지 구하기
def solution(num1, num2):
    return num1 % num2

# 중앙값 구하기
def solution(array):
    array.sort()
    return array[len(array) // 2 ]

# 최빈값 구하기
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1

# 짝수는 싫어요
def solution(n):
    arr = []
    for i in range(n+1):
        if i % 2 != 0:
            arr.append(i)
    return arr


# Day 4 수학, 배열
# 피자 나눠 먹기(1)
def solution(n):
    if n % 7 == 0:
        return n // 7
    else:
        return n // 7 + 1

# 피자 나눠 먹기(2)
def solution(n):
    if n % 6 == 0:
        return n // 6
    else:
        for i in range(1, 100):
            if (n * i) % 6 == 0:
                return (n * i) // 6


# 피자 나눠 먹기(3)
def solution(slice, n):
    if n % slice == 0:
        return n // slice
    else:
        return n // slice + 1

def solution(slice, n):
    return n // slice if n % slice == 0 else n // slice + 1

# 배열의 평균값
def solution(numbers):
    return sum(numbers) / len(numbers)
    

# Day 5 수학, 배열
# 옷가게 할인 받기
def solution(price):
    if 100000 <= price < 300000:
        price = price - price * 0.05
    elif 300000 <= price < 500000:
        price = price - price * 0.1
    elif price >= 500000:
        price = price - price * 0.2
    return int(price)

# 아이스 아메리카노
def solution(money):
    cnt = exchange = 0
    cnt = money // 5500
    exchange = money % 5500
    return [cnt, exchange]

# 나이 출력
def solution(age):
    return 2022 - age + 1

# 배열 뒤집기
def solution(num_list):
    return list(reversed(num_list))

def solution(num_list):
    num_list.reverse()
    return num_list

def solution(num_list):
    return num_list[::-1]

# Day 6 문자열, 반복문, 출력, 배열, 조건문
# 문자열 뒤집기
def solution(my_string):
    return my_string[::-1]


# 직각삼각형 출력하기
n = int(input())
for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print('')


# 짝수 홀수 개수
def solution(num_list):
    odd_cnt = 0
    even_cnt = 0
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1
    answer = [even_cnt, odd_cnt]
    return answer


# 문자 반복 출력하기
def solution(my_string, n):
    answer = []
    
    for i in range(0, len(my_string)):
        answer.append(my_string[i] * n)
        
    answer = ''.join(answer)
    return answer


# Day 7 문자열, 조건문, 수학, 반복문
# 특정 문자 제거하기
def solution(my_string, letter):
    return my_string.replace(letter,'')


# 각도기
def solution(angle):
    idx = 0
    if 0 < angle < 90:
        idx = 1
    elif angle == 90:
        idx = 2
    elif 90 < angle < 180:
        idx = 3
    elif angle == 180:
        idx = 4
    return idx


# 양꼬치
def solution(n, k):
    result = (12000 * n) + (2000 * k) - ((n // 10) * 2000)
    return result


# 짝수의 합
def solution(n):
    answer = 0
    for i in range(n+1):
        if i % 2 == 0:
            answer += i
    return answer

# Day 8 배열, 구현, 수학
# 배열 자르기



# 외계행성의 나이
def solution(age):
    answer = ''
    li = list(str(age))
    for i in range(len(li)):
        if li[i] == '0':
            answer += 'a'
        elif li[i] == '1':
            answer += 'b'
        elif li[i] == '2':
            answer += 'c'
        elif li[i] == '3':
            answer += 'd'
        elif li[i] == '4':
            answer += 'e'
        elif li[i] == '5':
            answer += 'f'
        elif li[i] == '6':
            answer += 'g'
        elif li[i] == '7':
            answer += 'h'
        elif li[i] == '8':
            answer += 'i'
        elif li[i] == '9':
            answer += 'j'
    return answer
solution(23)


# 진료순서 정하기
 def solution(emergency):
    arr = sorted(emergency, reverse=True)
    
    answer = []
    for i in emergency:
        answer.append(arr.index(i)+1)     
    return answer


# 순서쌍의 개수



# Day 9 수학, 문자열, 해시, 완전탐색, 조건문
# 개미 군단



# 모스 부호(1)



# 가위 바위 보



# 구슬을 나누는 경우의 수



