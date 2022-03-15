scoville = [1, 2, 3, 9, 10, 12]
K = 7
cnt = 0
scoville.sort()
while(scoville[0] < K):
    if len(scoville) == 1 and scoville[0] < K:
        print(-1)
        exit(0)
    a = scoville.pop(0)
    b = scoville.pop(0)
    scoville.append(a+b*2)
    scoville.sort()
    cnt += 1
    
    
print(cnt)