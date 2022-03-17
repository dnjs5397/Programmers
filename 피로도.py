from itertools import permutations

k = 80
result = 0
dungeons = [[80,20],[50,40],[30,10]]
real_dungeons = list(permutations(dungeons, len(dungeons)))
for i in real_dungeons:
    cnt = 0
    tmp_k = k
    for j in i:
        if tmp_k < j[0]:
            continue
        tmp_k -= j[1]
        cnt += 1
    result = max(result, cnt)

print(result)