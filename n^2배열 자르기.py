n = 3
left = 2
right = 5
answer = []
ll = left // n
rr = right // n
for i in range(ll, rr+1):
    tmp = []
    num = i+1
    while (len(tmp) < n):
        for j in range(num):
            tmp.append(num)
            if len(tmp) == n:
                break
        while (len(tmp) < n):
            num += 1
            tmp.append(num)
    answer += tmp

print(answer[left%n:left%n+right-left+1])