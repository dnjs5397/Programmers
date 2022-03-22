skill = "CBD"
count = 0
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
for i in skill_trees:
    skilltree = [k for k in skill]
    isright = True
    for j in i:
        if j in skill:
            if skilltree[0] == j:
                skilltree.pop(0)
            else:
                isright = False
    if isright == True:
        count += 1

print(count)