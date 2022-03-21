### eval() 함수를 사용하면 수식이 그대로 나옴

s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
answer = []
tmp = []

index = 0
while index < len(s)-1:
    if s[index] != '{' and s[index] != '}' and s[index] != ',':
        w = s[index]
        while s[index+1] != '{' and s[index+1] != '}' and s[index+1] != ',':
            index += 1
            w += s[index]
        tmp.append(int(w))
    if s[index] == '}':
        if len(tmp) != 0:
            answer.append(tmp)
            tmp = []
    index += 1
            
answer.sort(key = lambda x : len(x))
arr = []
while len(answer) > 0:
    num = answer[0][0]
    answer.pop(0)
    arr.append(num)
    for i in range(len(answer)):
        answer[i].remove(num)

print(arr)