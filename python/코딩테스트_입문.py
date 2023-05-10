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


# 피자 나눠 먹기(3)


# 배열의 평균값


