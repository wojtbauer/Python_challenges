#Question 2

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Factorial = int(input("Wpisz liczbę: "))
# wynik = 1
#
# #if/elif solution! - option 1
# if Factorial < 0:
#     print("Wstaw wartość nieujemną!")
# elif Factorial == 0:
#     print("0! = 1")
# else:
#     for i in range(1, Factorial+1):
#         wynik = wynik*i
#     print(Factorial, wynik)

#while solution! - option 2
# while Factorial > 0:
#     wynik = wynik * Factorial
#     Factorial = Factorial - 1
# print(wynik)

#Function solution - option 3
def Fact(x):
    if x == 0:
        return 1
    elif x > 0:
        return x * Fact(x-1)

x = int(input("Wpisz liczbę: "))
print(Fact(x))