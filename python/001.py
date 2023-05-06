def solution(a, b, c):
    cnt = 0
    if a != b != c:
        cnt = a + b + c
    elif a != b == c or a == b != c or a == c != b:
        cnt = (a + b + c) * ((a ** 2)+ (b ** 2) + (c ** 2))
    elif a == b == c:
        cnt = (a + b + c) * ((a ** 2)+ (b ** 2) + (c ** 2)) * ((a ** 3)+ (b ** 3) + (c ** 3))
    return cnt