genres = ["classic", "pop", "classic", "classic", "pop"]

plays = [500, 600, 150, 800, 2500]

answer = []
g1 = {}
for i in range(len(plays)):
    if genres[i] in g1:
        g1[genres[i]] += plays[i]
    else:
        g1[genres[i]] = 0
        g1[genres[i]] += plays[i]

s_genre = sorted(g1.items(), reverse=True)

g2 = [ [] for _ in range(len(s_genre)) ]
for i in range(len(s_genre)):
    for j in range(len(plays)):
        if genres[j] == s_genre[i][0]:
            g2[i].append((j, plays[j]))
            
for i in g2:
    i = i.sort(key = lambda x : x[1], reverse=True)
    
for i in g2:
    if len(i) == 1:
        answer.append(i[0][0])
    elif len(i)%2 == 0:
        for j in i:
            answer.append(j[0])
    elif len(i)%2 == 1:
        i.pop()
        for j in i:
            answer.append(j[0])

print(answer)