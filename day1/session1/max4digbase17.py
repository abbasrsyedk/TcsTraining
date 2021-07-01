# given a maximum of four digits to the base 17(10-A, 11-B, 12-C, 16-G)
# as input, output its decimal value
import math
values = dict({"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
               "9": 9, "0": 0, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16})


def spliter(word):
    return [char for char in word]


inp = input()
sinp = tuple(x for x in spliter(inp))
p = len(inp)-1
sum = 0
for _ in sinp:
    sum += values.get(_)*(math.pow(17, p))
    p -= 1
print(sum)
