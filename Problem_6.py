# Question:

# Write a program that calculates and prints the value according to the given formula:
# Q = sqrt[(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

import math
#simple example!
# C = 50
# H = 30
# D = float(input("Wpisz wartość: "))
# Q = round(math.sqrt((2*C*D)/H))
# print(Q)

C = 50
H = 30
inTab = [float(x) for x in input("Wpisz dane na listę: ").split(',')]
outTab = []
for D in inTab:
    outTab.append(str(round(math.sqrt((2*C*D)/H))))

sign = ', '
print(sign.join(outTab))