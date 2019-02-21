# expression
total: int = 0
for n in range(1, 51):
    total += ((-1)**(n-1))*(n**2)
print(total)
print()

# factor
num = eval(input('Input number:'))
for i in range(1, num+1):
    if num % i == 0:
        print(i)
print()

# perfect number
for i in range(1, 101):
    total = 0
    for j in range(1, i):
        if i % j == 0:
            total += j
    if total == i:
        print(total)
print()

# armstrong
for i in range(1, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if 100*i + 10*j + k == i**3 + j**3 + k**3:
                print('{}{}{}'.format(i, j, k))
print()

# prime
n = eval(input('Input a number: '))
for i in range(2, n):                                               # 1
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
print()

print([n for n in range(2, n) if all(n % i for i in range(2, n))])  # 2
print()
# rope
days = 0
rope = 3000
while rope >= 5:
    days += 1
    rope = rope / 2
print(days)
print()

# rabbit
n = 2
while n % 3 != 1:
    n += 1
    while n % 5 != 3:
        n += 1
        while n % 7 != 2:
            n += 1
print(n)

# password
password = 820904
num = eval(input('請輸入密碼:'))
if num == password:
    print('密碼輸入正確，歡迎使用本系統！')
else:
    num = eval(input('請輸入密碼:'))
    if num == password:
        print('密碼輸入正確，歡迎使用本系統！')
    else:
        num = eval(input('請輸入密碼:'))
        if num == password:
            print('密碼輸入正確，歡迎使用本系統！')
        else:
            print('密碼輸入超過三次!')
print()

# stars
# (1)
for i in range(1, 6):
    print('*'*i)
print()
# (2)
for i in range(1, 6):
    print('*'*(6-i))
print()
# (3)
for i in range(1, 6):
    print(' '*(5-i), ' *'*i)
print()

# nineNine
for i in range(9, 0, -1):
    for j in range(1, i+1):
        print(i*j, end=' ')
    print()

# interest
n = 0
p = 100000
q = 100000
while p >= q:
    p += 10000
    q *= (1+0.05)
    n += 1
print('錢精打:', p, '郝細算:', q, n, '年')

# loan
# 銀行
amount_y = 100000
rate_y_m = 20/100/12
# 當鋪
amount_m = 100000
rate_m = 10/100
# 錢莊
amount_d = 100000
rate_d_m = (1/100)*30

a = amount_y * (1+rate_y_m)
b = amount_m * (1+rate_m)
c = amount_d * (1+rate_d_m)
print('一個月     銀行:', round(a), ' 當鋪:', round(b), ' 地下錢莊:', round(c))

for i in range(1, 13):
    amount_y += amount_y * rate_y_m
    amount_m += amount_m * rate_m
    amount_d += amount_d * rate_d_m
print('一年       銀行:', round(amount_y), ' 當鋪:', round(amount_m), ' 地下錢莊:', round(amount_d))
