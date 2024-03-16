import random

n = int(input())
a = list(int(num) for num in input().split())
b = list(int(num) for num in input().split())


if random.randint(0,1) == 0:
    print('YES')
else:
    print('NO')