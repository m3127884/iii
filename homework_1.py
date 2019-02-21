# season
month = eval(input('Input month'))
if 1 <= month <= 12:
    if 3 <= month <= 5:
        print('春')
    elif 6 <= month <= 8:
        print('夏')
    elif 9 <= month <= 11:
        print('秋')
    else:
        print('冬')
else:
    print('輸入錯誤')

# salary
hours = eval(input('Input hours'))
if hours <= 60:
    print(60*120)
elif hours <= 80:
    print(60*120 + (hours-60)*120*1.25)
else:
    print(60*120 + 20*120*1.25 + (hours-80)*120*1.5)

# electricity
kWh = eval(input('Input kWh'))
if kWh <= 240:
    money = kWh*01.5
elif kWh <= 540:
    money = 240*0.15 + (kWh-240)*0.25
else:
    money = 240*0.15 + 300*0.25 + (kWh-540)*0.45
print('Household {0}    Industrial {1}' .format(money, kWh*0.45))

# leap year
year = eval(input('Input year'))
if year % 4000 == 0:
    print("非閏年")
else:
    if year % 400 == 0:
        print("閏年")
    else:
        if year % 100 == 0:
            print("非閏年")
        else:
            if year % 4 == 0:
                print("閏年")
            else:
                print("非閏年")

# refund
payable, paid = eval(input('Input payable and paid'))
change = paid - payable
thousand = change // 1000
fiveh = (change - thousand*1000) // 500
hundred = (change - thousand*1000 - fiveh*500) // 100
fifty = (change - thousand*1000 - fiveh*500 - hundred*100) // 50
ten = (change - thousand*1000 - fiveh*500 - hundred*100 - fifty*50) // 10
five = (change - thousand*1000 - fiveh*500 - hundred*100 - fifty*50 - ten*10) // 5
one = (change - thousand*1000 - fiveh*500 - hundred*100 - fifty*50 - ten*10 - five*5)
if paid < payable:
    print('金額不足')
elif paid == payable:
    print('不必找錢')
else:
    print('付', paid, '元'' 應找回', thousand, '張1000元', fiveh, '張500元', hundred, '張100元',
          fifty, '個50元', ten, '個10元', five, '個5元', one, '個1元')

# equation
a, b, c = eval(input('If ax^2 + bx + c = 0\n Input a,b,c find x'))
if b**2 - 4*a*c > 0:
    print('x =', (-b+(b**2 - 4*a*c)**0.5)/(2*a), (-b-(b**2 - 4*a*c)**0.5)/(2*a))
elif b**2 - 4*a*c == 0:
    print('x有兩個想同實根  x =', (-b+(b**2 - 4*a*c)**0.5)/(2*a))
else:
    print('沒有實根')
