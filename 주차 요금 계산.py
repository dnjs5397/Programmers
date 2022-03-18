fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", 
           "06:00 0000 IN", 
           "06:34 0000 OUT",
           "07:59 5961 OUT", 
           "07:59 0148 IN", 
           "18:59 0000 IN", 
           "19:09 0148 OUT", 
           "22:59 5961 IN", 
           "23:00 5961 OUT"]

parking = {}
fee = {}
for i in records:
    tmp = i.split(' ')
    if tmp[2] == 'IN':
        parking[tmp[1]] = tmp[0].replace(':', '')
        if tmp[1] not in fee:
            fee[tmp[1]] = 0
    else:
        outhour = int(tmp[0][0]+tmp[0][1]) # 출차 시간
        outmin = int(tmp[0][-2]+tmp[0][-1]) # 출차 분
        inhour = int(parking[tmp[1]][0] + parking[tmp[1]][1])
        inmin = int(parking[tmp[1]][2] + parking[tmp[1]][3])
        hour = outhour-inhour
        min = outmin-inmin
        if min < 0:
            hour -= 1
            min += 60
        time = min + hour*60
        fee[tmp[1]] += time
        del(parking[tmp[1]])

for i in parking:
    outhour = 23
    outmin = 59
    inhour = int(parking[i][0] + parking[i][1])
    inmin = int(parking[i][2] + parking[i][3])
    hour = outhour-inhour
    min = outmin-inmin
    if min < 0:
        hour -= 1
        min += 60
    time = min + hour*60
    fee[i] += time
answer = []
car = sorted(fee.items())
for i in car:
    time = i[1]
    if time <= fees[0]:
        answer.append(fees[1])
    else:
        time -= fees[0]
        if time % fees[2] == 0:
            answer.append(fees[1] + (time//fees[2])*fees[3])
        else:
            answer.append(fees[1] + (time//fees[2]+1)*fees[3])
            
print(answer)