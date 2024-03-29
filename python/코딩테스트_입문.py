# Day 1 사칙연산
# 두 수의 합
import re
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
    return array[len(array) // 2]

# 최빈값 구하기
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0:
            return a
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
    return my_string.replace(letter, '')


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
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]


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


# 진료순서 정하기
def solution(emergency):
    arr = sorted(emergency, reverse=True)

    answer = []
    for i in emergency:
        answer.append(arr.index(i)+1)
    return answer


# 순서쌍의 개수
def solution(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    return cnt


# Day 9 수학, 문자열, 해시, 완전탐색, 조건문
# 개미 군단
def solution(hp):
    # 장군개미의 공격력 a, 병정개미의 공격력 b, 일개미의 공격력 c
    a, b, c = 5, 3, 1

    # 개미의 수를 최대한 줄이기 위해 장군개미를 최대한으로 사용
    max_a_count = hp // a
    min_count = hp

    # 모든 경우의 수 계산
    for a_count in range(max_a_count, -1, -1):
        for b_count in range((hp - a_count * a) // b, -1, -1):
            c_count = hp - (a_count * a) - (b_count * b)
            if c_count >= 0 and c_count % c == 0:
                total_count = a_count + b_count + (c_count // c)
                if total_count < min_count:
                    min_count = total_count

    return min_count


def solution(hp):
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)


# 모스 부호(1)
def solution(letter):
    morse = {
        '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
        '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
        '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
        '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
        '-.--': 'y', '--..': 'z'
    }
    answer = ""
    codes = letter.split()
    for i in codes:
        answer += morse[i]

    return answer


# 가위 바위 보
def solution(rsp):
    answer = ''
    for i in rsp:
        if i == '2':
            answer += '0'
        elif i == '0':
            answer += '5'
        elif i == '5':
            answer += '2'
    return answer


def solution(rsp):
    d = {'0': '5', '2': '0', '5': '2'}
    return ''.join(d[i] for i in rsp)

# 구슬을 나누는 경우의 수
def solution(balls, share):
    return fact(balls) / (fact(share) * fact(balls-share))


def fact(x):
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

# Day 10 조건문, 배열, 수학, 시뮬레이션
# 점의 위치 구하기
def solution(dot):
    standard = 0
    if dot[0] > standard:
        if dot[1] > standard:
            return 1
        else:
            return 4
    else:
        if dot[1] > standard:
            return 2
        else:
            return 3


# 2차원으로 만들기
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer

# 공 던지기
def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]

# 배열 회전시키기
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]


# Day 11 수학, 반복문
# 주사위의 갯수
def solution(box, n):
    a = box[0] // n
    b = box[1] // n
    c = box[2] // n
    return a * b * c


# 합성수 찾기
def solution(n):
    cnt = 0
    answer = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt >= 3:
            answer += 1
        cnt = 0
    return answer

# 최댓값 만들기(1)
def solution(numbers):
    a = max(numbers)
    numbers.remove(a)
    b = max(numbers)
    answer = a * b
    return answer


# 팩토리얼
def solution(n):
    answer = 1
    factorial = 1
    while factorial <= n:
        answer += 1
        factorial = factorial * answer
    answer -= 1
    return answer

# Day 12 문자열, 정렬, 사칙연산, 수학
# 모음제거
def solution(my_string):
    string = 'aeiou'
    for i in string:
        my_string = my_string.replace(i, '')
    return my_string


# 문자열 정렬하기(1)
def solution(my_string):
    l = []
    for i in my_string:
        if i.isdigit() == True:
            l.append(int(i))
    return sorted(l)


# 숨어있는 숫자의 덧셈(1)
def solution(my_string):
    return sum([int(i) for i in re.sub('[^1-9]', '', my_string)])

# 소인수분해
def solution(n):
    answer = []
    i = 2
    while 1:
        if n == 1:
            return answer
        elif n % i == 0:
            n = n / i
            if i not in answer:
                answer.append(i)
        elif n % i != 0:
            i += 1

# Day 13 문자열, 배열, 사칙연산, 수학, 조건문
# 컨트롤 제트
def solution(s):
    arr = s.split(' ')
    result = []
    for i in arr:
        if i == 'Z':
            result.pop()
        else:
            result.append(int(i))
    return sum(result)

# 배열 원소의 길이
def solution(strlist):
    length = []
    for i in strlist:
        length.append(len(i))
    return length

# 중복된 문자 제거
def solution(my_string):
    result = ''
    for i in my_string:
        if i not in result:
            result += i
    return result

# 삼각형의 완성조건(1)
def solution(sides):
    m = 0
    n = 0
    for i in sides:
        n += i
        if i > m:
            m = i
    return 1 if m < n-m else 2


# Day 14 조건문, 반복문, 시뮬레이션, 문자열
# 가까운 수
def solution(array, n):
    array.sort()
    temp = []

    for i in array :
        temp.append( abs(n-i) )
    # abs() - 절댓값 구하는 함수
    return array[temp.index(min(temp))]


# 369게임
def solution(order):
    return str(order).count('3') + str(order).count('6') + str(order).count('9')

def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))


# 암호 해독
def solution(cipher, code):
    answer = ''
    for i in range(code-1, len(cipher), code):
        answer += cipher[i]

    return answer

def solution(cipher, code):
    return cipher[code-1::code]


# 대문자와 소문자
def solution(my_string):
    answer = ''
    # ord()는 문자의 아스키코드 번호를 출력 ord('A') = 65
    # chr()는 아스키코드 번호를 문자로 출력 chr(65) = A 
    for i in range(len(my_string)):
        if 64 <= ord(my_string[i]) < 97: #대문자면
            answer += chr(ord(my_string[i]) + 32)
        elif 97 <= ord(my_string[i]) < 123:
            answer += chr(ord(my_string[i]) - 32)
    return answer
    

# Day 15 문자열, 해시, 배열, 수학
# 영어가 싫어요
def solution(numbers):
    numbers = numbers.replace('zero', '0').replace('one', '1').replace('two', '2').replace('three', '3').replace('four', '4').replace('five', '5').replace('six', '6').replace('seven', '7').replace('eight', '8').replace('nine', '9')
    return int(numbers)

    # 밑에 풀이가 내가 원했던거..
def solution(numbers):
    r = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for k in r.keys():
        numbers = numbers.replace(k, r[k])

    return int(numbers)

# 인덱스 바꾸기
def solution(my_string, num1, num2):
    li = list(my_string)
    li[num1],li[num2] = li[num2],li[num1]
    return ''.join(li)


# 한 번만 등장한 문자
def solution(s):
    li = []
    for i in s:
        if s.count(i) == 1:
            li.append(i)
            li = sorted(li)
    return ''.join(li)


# 약수 구하기
def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer.append(i)
    return answer

# Day 16 문자열, 수학, 배열, 조건문
# 편지
def solution(message):
    return len(message)*2


# 가장 큰 수 찾기
def solution(array):
    answer = []
    answer.append(max(array))
    answer.append(array.index(max(array)))
    return answer

def solution(array):
    return [max(array), array.index(max(array))]

# 문자열 계산하기
def solution(my_string):
    answer = 0
    tmp = my_string.split()
    answer += int(tmp[0])
    for i in range(1,len(tmp)+1):
        if i != len(tmp):
            if tmp[i] == '+':
                answer += int(tmp[i+1])
            elif tmp[i] == '-':
                answer -= int(tmp[i+1])
            else:
                continue
    return answer


# 배열의 유사도
def solution(s1, s2):
    answer = 0
    for i in s1:
        if i in s2:
            answer += 1
    return answer

# Day 17 문자열, 수학, 조건문, 배열, 사칙연산
# 숫자 찾기
def solution(num, k):
    answer = 0
    snum = str(num)
    sk = str(k)
    if sk in snum:
        return snum.find(sk) + 1
    else:
        return -1


# n의 배수 고르기
def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
    return answer


# 자릿수 더하기
def solution(n):
    answer = 0
    li = list(str(n))
    for i in li:
        answer += int(i)
    return answer


# OX퀴즈
# 얘는 런타임에러가 난다...
def solution(quiz):
    arr_quiz = []
    answer = []
    left = []
    code = ''
    
    for i in range(len(quiz)):
        arr_quiz = quiz[i].replace(' ','').split('=')
        if '+' in arr_quiz[0]:
            left = arr_quiz[0].split('+')
            code = '+'
        elif '-' in arr_quiz[0]:
            left = arr_quiz[0].split('-')
            code = '-'
        if code == '+':
            if (int(left[0]) + int(left[1])) == int(arr_quiz[1]):
                answer.append('O')
            else:
                answer.append('X')
        elif code == '-':
            if (int(left[0]) - int(left[1])) == int(arr_quiz[1]):
                answer.append('O')
            else:
                answer.append('X')
    
    return answer

def solution(quiz):
    answer = []
    
    for i in quiz:
        l, r = i.split(' = ')
        a, code, b = l.split()
        if code == '+':
            result = 'O' if int(a) + int(b) == int(r) else 'X'
            answer.append(result)
        else:
            result = 'O' if int(a) - int(b) == int(r) else 'X'
            answer.append(result)
        
    return answer


# Day 18 문자열, 수학, 조건문, 정렬
# 문자열안에 문자열
def solution(str1, str2):
    return 1 if str2 in str1 else 2


# 제곱수 판별하기
def solution(n):
    m = n/2
    for i in range(1000):
        m -= i
        if m < i:
            if m*2 == i+1:
                return 1
            else: return 2

def solution(n):
    for i in range(1, n):
        if n == i * i:
            return 1
    return 2


# 세균 증식
def solution(n, t):
    for i in range(t):
        n *= 2
    return n


# 문자열 정렬하기 (2)
def solution(my_string):
    n = list(my_string.lower())
    return ''.join(sorted(n))

# Day 19 문자열, 배열, 조건문
# 7의 개수
def solution(array):
    answer = 0
    for i in array:
        answer += str(i).count('7')
    return answer


# 잘라서 배열로 저장하기
def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+n])
    return answer


# 중복된 숫자 개수
def solution(array, n):
    return array.count(n)


# 머쓱이보다 키 큰 사람
def solution(array, height):
    cnt = 0
    for i in array:
        if i > height:
            cnt += 1
    return cnt

# Day 20 수학, 시뮬레이션, 문자열, 사칙연산
# 직사각형 넓이 구하기
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])


# 캐릭터의 좌표
def solution(keyinput, board):
    col = board[0]
    row = board[1]
    result = [0, 0]
    for i in keyinput:
        if i == "left" and result[0]-1 >= -(col // 2):
            result[0] -= 1
        elif i == "right" and result[0]+1 <= (col // 2):
            result[0] += 1
        elif i == "up" and result[1]+1 <= (row // 2):
            result[1] += 1
        elif i == "down" and result[1]-1 >= -(row // 2):
            result[1] -= 1
    return result


# 최댓값 만들기 (2)
def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])


# 다항식 더하기
import re

def solution(polynomial):
    answer = ''
    lst = polynomial.split()

    const = 0
    coef = 0

    for i in lst[::2]:
        print(i)
        if 'x' not in i:
            const += int(i)
        else:
            if i == 'x':
                coef += 1 
            else:
                reg = re.compile('[0-9]{1,}')
                coef += int(reg.match(i)[0])

    print('coefficient:',coef,'const:',const)

    if coef == 0:
        answer += str(const)

    elif coef == 1:
        if const != 0:
            answer += 'x' 
            answer += ' + '
            answer += str(const)
        else:
            answer += 'x' 

    else:
        if const != 0:
            answer += str(coef)
            answer += 'x' 
            answer += ' + '
            answer += str(const)
        else:
            answer += str(coef)
            answer += 'x' 

    return answer


# Day 21 문자열, 사칙연산, 시뮬레이션, 2차원배열, 수학, 배열
# 숨어있는 숫자의 덧셈 (2)
import re

def solution(my_string):
    return sum(map(int, re.findall(r'[0-9]+', my_string)))


# 안전지대
def solution(board):
    count = 0
    row = [-1, 0, 1]
    col = [-1, 0, 1]
    danger_zone = [[0] * len(board) for _ in range(len(board))] 
    danger_zone_index = []
    for r in row:
        for c in col:
            danger_zone_index.append((r, c))

    # 지뢰 팔방을 danger_zone 만들기
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j] == 1:
                for x, y in danger_zone_index:
                    try:
                        if i+x < 0 or j+y < 0 or i+x > len(board) or j+y > len(board):
                            continue
                        danger_zone[i+x][j+y] = "x"
                    except:
                        continue
    for i, row in enumerate(danger_zone):
        for j, col in enumerate(row):
            if danger_zone[i][j] != "x":
                count += 1

    return count


# 삼각형의 완성조건 (2)
def solution(sides):
    sides.sort()
    m = max(sides)
    cnt = 0
    # 가장 긴 변이 sides 안에 있을때
    for i in range(m+1):
        if sides[0] + i > m:
            cnt += 1
    
    # 가장 긴 변이 나머지 한 변일 때
    for i in range(sum(sides)+1):
        if sides[1] < i and i < sum(sides):
            cnt += 1
    return cnt


# 외계어 사전
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2

# Day 22 dp, 수학, 조건문, 배열
# 저주의 숫자 3
def solution(n):
    count10 = 0
    count3 = 0
    while count10 < n:
        count10 += 1
        count3 += 1
        while count3 % 3 == 0 or '3' in str(count3):
            count3 += 1
    return count3


# 평행



# 겹치는 선분의 길이



# 유한소수 판별하기



# Day 23 배열, 정렬, 문자열
# 특이한 정렬




# 등수 매기기




# 옹알이 (1)
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



# 로그인 성공?



