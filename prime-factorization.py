factorial = int(input("Enter number to find factorial:   "))

tree = []
i = 2

while i < factorial:
    if (factorial/i)%1 == 0:
        tree.append(i)
        factorial = factorial/i
        i = 1
    i += 1

tree.append(int(factorial))

for i in range(len(tree)):
    print(str(tree[i]) + "    ")
