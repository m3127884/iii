# Maxmin
list1 = [51, 64, 81, 62, 94, 81, 12, 24, 31, 95]
list1.sort()
print('Min=', list1[:1], 'Max=', list1[-1:])

# passList
list2 = [[61, 52, 84, 30], [18, 79, 16, 46], [37, 49, 73, 20]]


def a():
    avg = (sum(list2[0])+sum(list2[1])+sum(list2[2]))/(len(list2[0])+len(list2[1])+len(list2[2]))
    return avg


def b():
    list_b = [max(list2[0]), max(list2[1]), max(list2[2])]
    max_list2 = max(list_b)
    return max_list2


def c():
    list_c = [min(list2[0]), min(list2[1]), min(list2[2])]
    min_list2 = min(list_c)
    return min_list2


def d():
    list_d = [sum(list2[0])/len(list2[0]), sum(list2[1])/len(list2[1]), sum(list2[2])/len(list2[2])]
    return list_d


def main():
    print(a())
    print(b())
    print(c())
    print(d())


main()

# sales
sales = ['Jean', 'Tom', 'Tina']
sale = [[32, 32, 56, 45, 32], [77, 32, 68, 45, 22], [42, 55, 42, 67, 65]]
money = [12, 16, 10, 14, 15]
item = ['A', 'B', 'C', 'D', 'E']
# a
salestotal = []
sum = 0
for i in range(0, 3):
    for j in range(0, 5):
        sum = sum + sale[i][j]*money[j]
    salestotal.append(sum)
    print(sales[i], sum)
print()
# b
best = salestotal.index(max(salestotal))
print(sales[best])
print()
# c
total_item = []
for i in range(5):
    total = (sale[0][i] + sale[1][i] + sale[2][i])*money[i]
    total_item.append(total)
print(total_item)

for i in range(5):
    print(item[i], total_item[i], '元')
print()
# d
best_item = total_item.index(max(total_item))
print(item[best_item])
print()

# rain
