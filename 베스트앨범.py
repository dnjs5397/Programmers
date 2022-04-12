genres = ["classic", "pop", "classic", "classic", "pop", "test"]

plays = [500, 600, 150, 800, 2500, 100]

answer = []
g1 = {}
for i in range(len(plays)):
    if genres[i] in g1:
        g1[genres[i]] += plays[i]
    else:
        g1[genres[i]] = 0
        g1[genres[i]] += plays[i]

s_genre = sorted(g1.items())
s_genre.sort(key = lambda x : x[1], reverse=True)

print(s_genre)
g2 = [ [] for _ in range(len(s_genre)) ]
for i in range(len(s_genre)):
    for j in range(len(plays)):
        if genres[j] == s_genre[i][0]:
            g2[i].append((j, plays[j]))
            
for i in g2:
    i.sort(key = lambda x : x[1], reverse=True)
    
print(g2)
for i in g2:
    if len(i) == 1:
        answer.append(i[0][0])
    else:
        answer.append(i[0][0])
        answer.append(i[1][0])

print(answer)