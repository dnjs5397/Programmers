import heapq

scoville = [1, 2, 3, 9, 10, 12]
heapq.heapify(scoville)
K = 7
cnt = 0
while(len(scoville) >= 2):
    a = heapq.heappop(scoville)
    if a >= K:
        print(cnt)
        exit(0)
    
    b = heapq.heappop(scoville)
    heapq.heappush(scoville, a+b*2)
    cnt += 1

if scoville[0] >= K:
    print(cnt)
else:
    print(-1)