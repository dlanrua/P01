Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # E01
a, b = map(int, input().split())
print(a*b)
# E02
a = 1.2345
print(f'{a:.2f}')
# E03
a, b = map(int, input('더한거 뺀거 곱한거 몫 나머지').split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
# E04
a=int(input('정수 1: '))
b=int(input('정수 2: '))
if a>b:
    print('큰 수는', a, '이고, 작은 수는', b, '이다')
else:
    print('큰 수는', b, '이고, 작은 수는', a, '이다')
# E05
score = int(input('점수: '))
if score>=80:
    print('합격')
else:
    print('불합격')
# E06
n = int(input('0인지 양수인지 음수인지 판별하는 기계'))
if n>0:
    print('양수')
elif n==0:
    print('0')
else:
    print('음수')
# E07
a, b = map(int, input('a부터 b까지 수의 합').split())

t=0
while a<=b:
    t=t+a
    a=a+1
print(t)
# E08
a=1
b=10
while b>=a:
    print(b, end=' ')
    b=b-1
# E09  
a = int(input('배수 10개 출력'))
c = 1
while c<=10:
    print(a*c, end=' ')
    c=c+1
# E10
a = int(input('구구단 출력'))
c = 1
while c<=9:
    print(a,'*',c,'=',a*c)
    c=c+1
# H01
a = int(input('첫 번째 수: '))
b = int(input('두 번째 수: '))
c = int(input('세 번째 수: '))
if a%2 == 1:
    print(a, '홀수')
else:
    print(a, '짝수')
if b%2 == 1:
    print(b, '홀수')
else:
    print(b, '짝수')
if c%2 ==1:
    print(c, '홀수')
else:
    print(c, '짝수')


# H03
a = int(input('사용량'))
b = int(input('등급'))
if b==1:
    c = a*535*1.03
    print('wlqnf rmador:', f'{c:.2f}')
elif b==2:
    c = a*377*1.03
    print('wlqnf rmador:', f'{c:.2f}')
elif b==3:
    c = a*291*1.03
    print('wlqnf rmador:', f'{c:.2f}')
else:
    print('wlqnf rmador: emdrmqdmf wkfaht dlqfurgoTtmqslek.')

# H04
a = int(input('age'))
b = int(input('price'))
if a<18 or a>=70:
    print('wlqnf rmador:', int(b*0.8), 'won')
elif 60<=a<70:
    print('wlqnf rmador:', int(b*0.85), 'won')
else:
    print('wlqnf rmador:', b, 'won')
# H05
a=1
t=0
while a<=100:
    if a%2==1:
        t=t+a
    elif a%2==0:
        t=t-a
    a=a+1
print(t)
# H06
c = 0
for n in range(1, 1001):
    c += str(n).c('5')

print("rotn:", c)

# H07

def count_digits(A, B, C):
    result = A * B * C
    result_str = str(result)
    digit_counts = [0] * 10

    for digit in result_str:
        digit_counts[int(digit)] += 1

    return digit_counts

A = int(input())
B = int(input())
C = int(input())

counts = count_digits(A, B, C)
for i in range(10):
    print(f"{counts[i]}")