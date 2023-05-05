def solution(n):
    x = 0
    for i in range(n):
        if (n % 2 == 0): 
            x += (n ** 2)
        else:
            x += n
    return answer