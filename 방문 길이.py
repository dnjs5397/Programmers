x,y = 0, 0
dirs = "UDUD"
answer = []
for i in range(len(dirs)):
    dx, dy = x,y
    direction = dirs[i]
    if direction == 'U':
        dy += 1
    elif direction == 'D':
        dy -= 1
    elif direction == 'L':
        dx -= 1
    else:
        dx += 1
    if dx > 5 or dx < -5 or dy > 5 or dy < -5:
        continue
    if (str(dx)+str(dy)+str(x)+str(y)) not in answer:
        answer.append(str(x)+str(y)+str(dx)+str(dy))
        x,y = dx, dy
    else:
        x,y = dx, dy

answer = list(set(answer))
print(answer)