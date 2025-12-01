# 과제 39
def a(n):
    for i in range(0, n+1):
        if i % 2 != 0:
            print(i)

b = int(input('양수 입력: '))
print(a(b))

# 과제 40
def a(n):
    for i in range(0, n+1):
        if i % 3 == 0:
            print(i)

b = int(input('숫자 입력: '))
print(a(b))

# 과제 41
def n(a, b, c, d):
    numbers = [a, b, c, d]
    return max(numbers), min(numbers)

a = int(input('숫자 입력: '))
b = int(input('숫자 입력: '))
c = int(input('숫자 입력: '))
d = int(input('숫자 입력: '))

max, min = n(a, b, c, d)
print('최댓값: ', max)
print('최솟값: ', min)

# 과제 42
def a(n):
    for i in range(0, n+1):
        if i % 2 != 0:
            print(i)

b = int(input('양수 입력: '))
print(a(b))

# 과제 43
def a(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

b = int(input("정수 n 입력: "))
print(a(b))

# 과제 44
def a(i, j):
    total = 0
    for x in range(1, i+1):
        for y in range(1, j+1):
            if x * y >= 30:
                total += x * y
    return total

i, j = map(int, input("2이상 9이하의 양수 2개 입력: ").split())
print(a(i, j))

# 과제 45
def a(n):
    result = []
    total = 0
    for i in n:
        total += i
        result.append(total)
    return result 
    
b = list(map(int, input("1, 2, 3, 4, 5를 입력: ").split()))
print(a(b))