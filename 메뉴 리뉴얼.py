import itertools
answer = []
course = [2,3,4]	
maxfood = []
food = {}
orders = ["XYZ", "XWY", "WXA"]
for i in orders:
    for j in course:
        tmp = list(itertools.combinations(i, j))
        if tmp:
            for k in tmp:
                dish = ''.join(sorted(k))
                if dish in food:
                    food[dish] += 1
                else:
                    food[dish] = 1
print(food)
result = sorted(food.items())
for i in course:
    val = 0
    for j in result:
        if len(j[0]) == i:
            val = max(val, j[1])
    maxfood.append(val)

for i in range(len(course)):
    for j in result:
        if len(j[0]) == course[i] and j[1] == maxfood[i] and maxfood[i] >= 2:
            answer.append(j[0])
            
print(sorted(answer))