class PythonSwitchStatement:

    def switch(self, c):
        return getattr(self, 'case_' + str(c))

    def case_R(self, x, distance, c):
        x = x+distance
        distance += 10
        c = 'U'

    def case_U(self, y, distance):
        y = y+distance
        c = 'L'
        distance += 10

    def case_L(self, x, distance):
        x = x-distance
        c = 'D'
        distance += 10

    def case_D(self, y, distance):
        y = y-distance
        c = 'U'
        distance += 10


s = PythonSwitchStatement()
c = "R"
distance = 10
x = 0
y = 0
n = int(input())
i = 1
while i < n:
    s.switch(c)
    i += 1
    distance += 10


print(x, y)
