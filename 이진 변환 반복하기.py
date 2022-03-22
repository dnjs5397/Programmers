s = "110010101001"
count = 0
delzero = 0
while (s != '1'):
    delzero += s.count('0')
    s = s.replace('0', '')
    num = int(len(s))
    num = bin(num)
    s = num[2:]
    count += 1

print([count, delzero])