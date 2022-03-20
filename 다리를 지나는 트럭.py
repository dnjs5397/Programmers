truck = [7,4,5,6]
weight = 10
bridge = 2
done = []
ing = []
length = len(truck)
count = 0
time = []
while (1):
    if len(done) == length and len(truck) == 0:
        break
    count += 1
    for i in range(len(time)):
        time[i] += 1
    for i in time:
        if i % bridge == 0 and i // bridge > 0:
            done.append(ing.pop(0))
            time.pop(0)
            break
    if len(truck) != 0:
        if sum(ing) + truck[0] <= weight:
            ing.append(truck.pop(0))
            time.append(0)
    

print(count)