# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

x = input("Wpisz tekst do analizy: ")
Upper = 0
Lower = 0
for a in x:
    if a.islower():
        Lower += 1
    if a.isupper():
        Upper += 1

print("Upper case is " + str(Upper))
print("Lower case is " + str(Lower))