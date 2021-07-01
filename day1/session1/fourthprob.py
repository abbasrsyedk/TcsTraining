
inp = int(input())


def spliter(n):
    return [int(d) for d in str(n)]


splittedinput = tuple(x for x in spliter(inp))
sumofeven = 0
sumofodd = 0
for a in splittedinput:
    if(a % 2 == 0):
        sumofeven += a
    else:
        sumofodd += a
print(sumofeven)
print(sumofodd)
# if(sumofeven > sumofodd):
#     print(sumofeven-sumofodd)
# else:
#     print(sumofodd-sumofeven)
print(abs(sumofodd-sumofeven))
