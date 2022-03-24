import re
import itertools
answer = []
expression = "100-200*300-500+20"
expression = re.split('([^0-9])', expression)
arr = ['-','+','*']
arr = list(itertools.permutations(arr, 3))
for i in arr:
    exp = expression.copy()
    for j in i:
        while j in exp:
            idx = exp.index(j)
            num = str(eval(exp[idx-1]+exp[idx]+exp[idx+1]))
            exp[idx] = num
            del exp[idx+1]
            del exp[idx-1]
    answer.append(abs(int(exp[0])))

print(max(answer))