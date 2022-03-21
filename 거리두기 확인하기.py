def con1(list, x,y): # 상하좌우 확인 - 사람 있으면 바로 끝
    global condition
    if x < 0 or x > 4 or y < 0 or y > 4 or condition == False:
        return
    if list[x][y] == 'P':
        condition = False
        return
    else:
        return
    
def con2(list, x,y): # 대각선 확인 - 사람이 있다면 사이에 가림막 있는지 확인
    global condition
    if condition == False:
        return
    dx, dy = x-1, y+1
    if dx < 0 or dx > 4 or dy < 0 or dy > 4:
        pass
    elif list[dx][dy] == 'P':
        if list[dx+1][dy] == 'X' and list[dx][dy-1] == 'X':
            pass
        else:
            condition = False
            return
    
    dx, dy = x+1, y-1
    if dx < 0 or dx > 4 or dy < 0 or dy > 4:
        pass
    elif list[dx][dy] == 'P':
        if list[dx-1][dy] == 'X' and list[dx][dy+1] == 'X':
            pass
        else:
            condition = False
            return
    
    dx, dy = x+1, y+1
    if dx < 0 or dx > 4 or dy < 0 or dy > 4:
        pass
    elif list[dx][dy] == 'P':
        if list[dx-1][dy] == 'X' and list[dx][dy-1] == 'X':
            pass
        else:
            condition = False
            return
    
    dx, dy = x-1, y-1
    if dx < 0 or dx > 4 or dy < 0 or dy > 4:
        pass
    elif list[dx][dy] == 'P':
        if list[dx+1][dy] == 'X' and list[dx][dy+1] == 'X':
            pass
        else:
            condition = False
            return
    
    return
    
def con3(list, x,y): # 상하좌우 2칸 확인
    global condition
    if condition == False:
        return
    dx, dy = x-2, y
    if dx < 0 or dx > 4 or dy < 0 or dy > 4:
        pass
    elif list[dx][dy] == 'P':
        if list[dx+1][dy] == 'X':
            pass
        else:
            condition = False
            return
        
    dx, dy = x+2, y
    if dx < 0 or dx > 4 or dy < 0 or dy > 4:
        pass
    elif list[dx][dy] == 'P':
        if list[dx-1][dy] == 'X':
            pass
        else:
            condition = False
            return
        
    dx, dy = x, y-2
    if dx < 0 or dx > 4 or dy < 0 or dy > 4:
        pass
    elif list[dx][dy] == 'P':
        if list[dx][dy+1] == 'X':
            pass
        else:
            condition = False
            return
        
    dx, dy = x, y+2
    if dx < 0 or dx > 4 or dy < 0 or dy > 4:
        pass
    elif list[dx][dy] == 'P':
        if list[dx][dy-1] == 'X':
            pass
        else:
            condition = False
            return

    return

places = ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]
condition = True
for k in places:
    for i in range(5):
        for j in range(5):
            if k[i][j] == 'P':
                con1(k, i-1, j)
                con1(k, i+1, j)
                con1(k, i, j-1)
                con1(k, i, j+1)
                con2(k, i, j)
                con3(k, i, j)
if condition == False:
    print(0)
else:
    print(1)
            