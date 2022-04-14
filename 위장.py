clothes = [["yellowhat", "headgear"], 
           ["bluesunglasses", "eyewear"], 
           ["green_turban", "headgear"]]

ha = {}

for i in clothes:
    if i[1] in ha:
        ha[i[1]] += 1
    else:
        ha[i[1]] = 1
answer = 1
for i in ha:
    answer *= (ha[i]+1)
    
print(answer-1)