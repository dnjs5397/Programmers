number = "1231234"
k = 3
numlist = []
for i in range(len(number)):
    numlist.append(int(number[i]))
numlist.sort(reverse=True)
answer = ''
for i in range(len(number)-k):
    answer += str(numlist[i])
print(answer)
# 1차 실패